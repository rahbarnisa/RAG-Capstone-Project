#initial code
#from openai import OpenAI
#from config import OPENAI_API_KEY

#client = OpenAI(api_key=OPENAI_API_KEY)

#response = client.chat.completions.create(
     #model="gpt-4o-mini",
     #messages=[
          #{"role":"user", "content": "Say hello like a support agent"}
     #]
#)

#print(response.choices[0].message.content)

#modified code for loader py
#from src.loader import load_all_pdfs

#docs = load_all_pdfs()

#print(f"Total pages loaded: {len(docs)}")

#for i in range(4): 
    #print("-----")
    #print(docs[i].page_content[:200])
    #print(docs[i].metadata)

#modified for chunking
#from src.loader import load_all_pdfs
#from src.chunking import chunk_documents

#docs = load_all_pdfs()
#chunks = chunk_documents(docs)

#print("Pages loaded:", len(docs))
#print("Chunks created:", len(chunks))

#print("\n--- SAMPLE CHUNK ---\n")
#print(chunks[0].page_content[:500])

#print("\n--- METADATA ---\n")
#print(chunks[0].metadata)

#modified for vector db
#from src.loader import load_all_pdfs
#from src.chunking import chunk_documents
#from src.vector_store import create_vector_store

#step1: load
#docs = load_all_pdfs()

#step2: chunk
#chunks = chunk_documents(docs)

#step3:buld vector db 
#db = create_vector_store(chunks)

#print("Vector DB created successfully!")

#TEST SEARCH
#query = "What is Good Manufacturing Practice in pharma?"

#results = db.similarity_search(query, k=3)

#print("\n--- TOP RESULTS ---\n")

#for i, doc in enumerate(results):
    #print(f"\nResult {i+1}")
    #print(doc.page_content[:300])
    #print(doc.metadata)

#modified for rag pipeline
#from src.loader import load_all_pdfs
#from src.chunking import chunk_documents
#from src.vector_store import create_vector_store
#from src.rag_pipelines import retrieve_documents, build_context, generate_answer

#Load+prepare
#docs = load_all_pdfs()
#chunks = chunk_documents(docs)
#db = create_vector_store(chunks)

#Ask question
#query = "What are GMP requirements for sterile manufacturing?"

#RAG pipeline
#retrieved_docs = retrieve_documents(query, db)
#context, sources = build_context(retrieved_docs)
#answer = generate_answer(query, context, sources)

#print("\n=== FINAL ANSWER ===\n")
#print(answer)

#App.py modified for memory
#from src.loader import load_all_pdfs
#from src.chunking import chunk_documents
#from src.vector_store import create_vector_store
#from src.rag_pipelines import retrieve_documents, build_context, generate_answer
#from src.memory import add_to_memory, get_memory

# Load system
#docs = load_all_pdfs()
#chunks = chunk_documents(docs)
#db = create_vector_store(chunks)

#print("AI Support Assistant Ready!\n")

#while True:
  #  query = input("You: ")

 #   if query.lower() == "exit":
 #       break

    # Retrieve
    #retrieved_docs = retrieve_documents(query, db)

    # Build context
    #context, sources = build_context(retrieved_docs)

    # Get memory
    #memory = get_memory()

    # Generate answer
    #answer = generate_answer(query, context, sources, memory)

    #print("\nAI:", answer)

    # Save memory
    #add_to_memory(query, answer)

#STREAMLIT APP PY CODE
import streamlit as st

from src.loader import load_all_pdfs
from src.chunking import chunk_documents
from src.vector_store import create_vector_store
from src.rag_pipelines import retrieve_documents, build_context, generate_answer
from src.memory import add_to_memory, get_memory

st.set_page_config(page_title="AI Pharma Support", layout="wide")

st.title("💊 AI Pharmaceutical Support Assistant")

# Load system once (cache)
@st.cache_resource
def load_system():
    docs = load_all_pdfs()
    chunks = chunk_documents(docs)
    db = create_vector_store(chunks)
    return db

db = load_system()

# Session state for chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask your question:")

if user_input:
    # Retrieve docs
    docs = retrieve_documents(user_input, db)

    # Build context
    context, sources = build_context(docs)

    # Get memory
    memory = get_memory()

    # Generate answer
    answer = generate_answer(user_input, context, sources, memory)

    # Save memory
    add_to_memory(user_input, answer)

    # Save to session UI
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", answer))

# Display chat
for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 AI:** {message}")