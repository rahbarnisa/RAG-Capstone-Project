from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()

    db = FAISS.from_documents(
       documents=chunks,
       embedding=embeddings
    )
    
    return db