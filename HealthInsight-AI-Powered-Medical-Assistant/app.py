import asyncio
from typing import List, Dict, Optional
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from transformers import pipeline
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.docstore.document import Document
import PyPDF2
from literalai import LiteralClient

import chainlit as cl
from chainlit.types import AskFileResponse
from chainlit.input_widget import TextInput

# Initialize Hugging Face medical model (e.g., PubMedBERT for medical Q&A)
qa_pipeline = pipeline("question-answering", model="microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract")


pinecone_index = "medicalbot"
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
pc = PineconeVectorStore(index_name=pinecone_index, embedding=embeddings)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

literalAI = LiteralClient()

welcome_message = """Welcome to the Medical Bot! To get started:
1. Upload PDF Reports
2. Ask a question about the reports

OR

Ask question about your medical condition
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
            max_files=3,
            timeout=3600
        ).send()

    docsearch = await get_docsearch(files)
    await cl.Message(content=f"Uploaded Reports!").send()
    # Reminder: The name of the pdf must be in the content of the message
    for file in files:
        await cl.Message(
                        content=f"{file.name}",
                        elements=[cl.Pdf(name=file.name, display="side", path=file.path, size='large')]
                        ).send()
    
    await cl.Message(content=f"You can now ask questions!").send()

    # keep checking until thread name is reflected in LiteralAI
    while not literalAI.api.get_thread(id=cl.context.session.thread_id):
        await asyncio.sleep(2)
    await setup_chat_name()


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
        msg = cl.Message(content=f"`{file.name}` processing...")
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


@cl.on_message
async def handle_message(message: cl.Message):
    files = message.elements
    if files:
        docsearch = await get_docsearch(files, append_new_docs=True)
        
        await cl.Message(content=f"Uploaded Reports!").send()
        # Reminder: The name of the pdf must be in the content of the message
        for file in files:
            await cl.Message(
                            content=f"{file.name}",
                            elements=[cl.Pdf(name=file.name, display="side", path=file.path, size='large')]
                            ).send()
        
        await cl.Message(content=f"You can now ask questions!").send()
        return

    # Handle medical question using the Hugging Face medical model (Q&A)
    question = message.content
    # Use the document search (Pinecone) and retrieve relevant documents
    pinecone_session_namespace = cl.user_session.get('pinecone_session_namespace')
    search_docs = pc.similarity_search(question, namespace=pinecone_session_namespace)
    print(search_docs)
    
    # Use Hugging Face pipeline to answer the medical question based on retrieved documents
    answer = qa_pipeline(question=question, context=search_docs[0].page_content)
    response = answer['answer']
    
    await cl.Message(content=f"Here is what I found: {response}").send()


def extract_text_from_pdf(file_path):
    reader = PyPDF2.PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


async def setup_chat_name():
    current_chat = literalAI.api.get_thread(id=cl.context.session.thread_id)
    initial_chat_name = current_chat.name if current_chat else ""
    await cl.ChatSettings(
        [
            TextInput(id="chat_name", label="Chat Name", initial=initial_chat_name, description='Note: The Chat name will update and reflect in the UI once the page is refreshed.'),
        ]
    ).send()


@cl.on_settings_update
async def on_settings_update(settings):
    initial_chat_name = literalAI.api.get_thread(id=cl.context.session.thread_id).name
    chat_name = settings['chat_name'] or initial_chat_name
    literalAI.api.update_thread(id=cl.context.session.thread_id, name=chat_name)


@cl.on_chat_resume
async def on_chat_resume():
    pineconde_session_namespace = cl.user_session.get('pinecone_session_namespace')
    docsearch = pc.from_existing_index(pinecone_index, embeddings, namespace=pineconde_session_namespace)
    await setup_chat_name()

