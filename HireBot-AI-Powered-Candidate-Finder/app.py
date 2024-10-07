import asyncio
from typing import List, Dict, Optional
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.docstore.document import Document

from literalai import LiteralClient

import chainlit as cl
from chainlit.types import AskFileResponse
from chainlit.input_widget import TextInput

pinecone_index = "hirebot"
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
pc = PineconeVectorStore(index_name=pinecone_index, embedding=embeddings)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

literalAI = LiteralClient()


welcome_message = """Welcome to the HireBot! To get started:
1. Upload PDF resumes
2. Ask a question about the resumes
"""


@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch the user matching username from your database
    # and compare the hashed password with the value stored in the database
    if (username, password) == ("admin", "admin"):
        return cl.User(identifier="admin", metadata={"role": "admin", "provider": "credentials"})
    else:
        return None
    

@cl.oauth_callback
def oauth_callback(provider_id: str, token: str, raw_user_data: Dict[str, str], default_user: cl.User) -> Optional[cl.User]:
  return default_user


def process_file(file: AskFileResponse):
    if any(
        [
            hasattr(file, 'type') and file.type == "application/pdf",
            hasattr(file, 'mime') and file.mime == "application/pdf"
        ]
    ):
        loader = PyPDFLoader(file.path)
        documents = loader.load()
        docs = text_splitter.split_documents(documents)
        for doc in docs:
            doc.metadata["source"] = f"{file.name}"
            doc.metadata["source_path"] = f"{file.path}"

        return docs


async def get_docsearch(files: List[AskFileResponse], append_new_docs=False):
    docs = []
    processing_messages = {}
    for file in files:
        msg = cl.Message(content=f"`{file.name}` processing...", disable_feedback=True)
        msg.persisted = True # think reverse. This will skip it to be persisted in LiteralAI
        await msg.send()
        processing_messages[file.name] = msg
        file_docs = process_file(file)
        docs.extend(file_docs)

    pineconde_session_namespace = cl.user_session.get('pinecone_session_namespace')
    print(pineconde_session_namespace)
    if append_new_docs:
        texts = [doc.page_content for doc in docs]
        metadatas = [doc.metadata for doc in docs]
        docsearch = pc.add_texts(texts, metadatas=metadatas, namespace=pineconde_session_namespace)
        docsearch = pc.from_existing_index(pinecone_index, embeddings, namespace=pineconde_session_namespace)
    else:
        docsearch = pc.from_documents(docs, embeddings, index_name=pinecone_index, namespace=pineconde_session_namespace)

    for file in files:
        processing_messages[file.name].content = ""
        await processing_messages[file.name].update()

    return docsearch


def setup_conversation_chain(docsearch: PineconeVectorStore):
    message_history = ChatMessageHistory()

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True,
    )
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5, streaming=True)
    retriever = docsearch.as_retriever(search_kwargs={'k': 7})

    chain = ConversationalRetrievalChain.from_llm(
        llm,
        chain_type="stuff",
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
    )

    return chain


@cl.on_settings_update
async def on_settings_update(settings):
    initial_chat_name = literalAI.api.get_thread(id=cl.context.session.thread_id).name
    chat_name = settings['chat_name'] or initial_chat_name
    literalAI.api.update_thread(id=cl.context.session.thread_id, name=chat_name)


async def setup_chat_name():
    current_chat = literalAI.api.get_thread(id=cl.context.session.thread_id)
    initial_chat_name = current_chat.name if current_chat else ""
    await cl.ChatSettings(
        [
            TextInput(id="chat_name", label="Chat Name", initial=initial_chat_name, description='Note: The Chat name will update and reflect in the UI once the page is refreshed.'),
        ]
    ).send()


@cl.on_chat_start
async def start():
    pinecone_session_namespace = f"{cl.user_session.get('user').identifier}-{cl.user_session.get('id')}"
    cl.user_session.set('pinecone_session_namespace', pinecone_session_namespace)
    files = None
    while files is None:
        files = await cl.AskFileMessage(
            content=welcome_message,
            accept=["application/pdf"],
            max_size_mb=5, # per file
            max_files=5,
            timeout=3600
        ).send()

    docsearch = await get_docsearch(files)
    chain = setup_conversation_chain(docsearch)
    
    await cl.Message(content=f"Uploaded Resumes!", disable_feedback=True).send()
    # Reminder: The name of the pdf must be in the content of the message
    for file in files:
        await cl.Message(
                        content=f"{file.name}",
                        disable_feedback=True,
                        elements=[cl.Pdf(name=file.name, display="side", path=file.path, size='large')]
                        ).send()
    
    await cl.Message(content=f"You can now ask questions!").send()
    cl.user_session.set("chain", chain)

    # keep checking until thread name is reflected in LiteralAI
    while not literalAI.api.get_thread(id=cl.context.session.thread_id):
        await asyncio.sleep(2)
    await setup_chat_name()   


@cl.on_message
async def on_message(message: cl.Message):
    files = message.elements
    if files:
        docsearch = await get_docsearch(files, append_new_docs=True)
        chain = setup_conversation_chain(docsearch)
        
        await cl.Message(content=f"Uploaded Resumes!", disable_feedback=True).send()
        # Reminder: The name of the pdf must be in the content of the message
        for file in files:
            await cl.Message(
                            content=f"{file.name}",
                            disable_feedback=True,
                            elements=[cl.Pdf(name=file.name, display="side", path=file.path, size='large')]
                            ).send()
        
        await cl.Message(content=f"You can now ask questions!").send()
        cl.user_session.set("chain", chain)
        return

    chain = cl.user_session.get("chain")  # type: ConversationalRetrievalChain
    cb = cl.AsyncLangchainCallbackHandler()
    res = await chain.ainvoke(message.content, callbacks=[cb])
    answer = res["answer"]
    source_documents = res["source_documents"]  # type: List[Document]

    await cl.Message(content=answer).send()

    if source_documents:
        sources = set((source_doc.metadata['source_path'], source_doc.metadata['source']) for source_doc in source_documents)
        await cl.Message(content='Sources:', disable_feedback=True).send()
        for source in sources:
            await cl.Message(
                        content=source[1], # resume name
                        disable_feedback=True,
                        elements=[cl.Pdf(name=source[1], display="side", path=source[0], size='large')]
                        ).send()



@cl.on_chat_resume
async def on_chat_resume():
    pineconde_session_namespace = cl.user_session.get('pinecone_session_namespace')
    docsearch = pc.from_existing_index(pinecone_index, embeddings, namespace=pineconde_session_namespace)
    chain = setup_conversation_chain(docsearch)
    cl.user_session.set("chain", chain)
    await setup_chat_name()

