from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
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
pc = PineconeVectorStore(index=pinecone_index, embedding=embeddings)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

literalAI = LiteralClient()



# Define the chatbot logic
@cl.on_chat_start
async def start():
    # Display welcome message and ask user to upload medical reports
    await cl.Message(
        content="Hello! I am your Medical Information Bot. Please upload your medical reports or ask any questions about medical conditions."
    ).send()

    # Request for file upload
    await cl.AskFileMessage(
        content="Please upload your medical reports (PDF format only) for analysis.",
        accept=["application/pdf"],
        max_files=3
    ).send()


def process_file(file: AskFileResponse):
    if file.type == "application/pdf":
        loader = PyPDFLoader(file.path)
        documents = loader.load()
        docs = text_splitter.split_documents(documents)
        for i, doc in enumerate(docs):
            doc.metadata["source"] = f"source_{i}"

        return docs


async def get_docsearch(files: List[AskFileResponse]):
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
    docsearch = pc.from_documents(docs, embeddings, index_name=pinecone_index, namespace=pineconde_session_namespace)

    for file in files:
        processing_messages[file.name].content = ""
        await processing_messages[file.name].update()

    return docsearch


# Handle file upload
@cl.on_message
async def handle_message(message: cl.Message):
    if message.files:
        for file in message.files:
            # Extract text from the uploaded medical PDF files
            pdf_text = extract_text_from_pdf(file.path)  # This function should handle the extraction
            documents = text_splitter.split_documents([pdf_text])

            # Embed the chunks and store them in Pinecone for future queries
            docs_with_embeddings = pc.add_documents(documents)
            
        await cl.Message(content="Your documents have been uploaded and processed. You can now ask any questions!").send()
    else:
        # Handle medical question using the Hugging Face medical model (Q&A)
        question = message.content
        if pc:
            # Use the document search (Pinecone) and retrieve relevant documents
            search_docs = pc.similarity_search(question)
            
            # Use Hugging Face pipeline to answer the medical question based on retrieved documents
            answer = qa_pipeline(question=question, context=search_docs[0].page_content)
            response = answer['answer']
            
            await cl.Message(content=f"Here is what I found: {response}").send()

# Helper function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    reader = PyPDF2.PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Chainlit loop for resume chat
@cl.on_resume_chat
async def on_resume():
    await cl.Message(content="Welcome back! Please feel free to ask more questions or upload new medical reports.").send()
