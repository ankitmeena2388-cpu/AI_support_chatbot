import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_vector_store(file_path: str):

    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split text properly (IMPORTANT FIX)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = splitter.split_documents(documents)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create FAISS DB
    db = FAISS.from_documents(docs, embeddings)

    # Save DB
    db.save_local("faiss_index")