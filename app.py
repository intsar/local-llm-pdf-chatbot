import os
import streamlit as st
import PyPDF2
from dotenv import load_dotenv
from langchain.llms import Ollama
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

load_dotenv()

# ---- Setup ----
persist_directory = "./chroma_store"

# Use local HuggingFace model
embedding_model = HuggingFaceEmbeddings(model_name=os.getenv("MODEL_PATH"))

# Load Ollama LLM
llm = Ollama(model="mistral")

# Load Vector Store (create if not exists)
if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)
    db = None
else:
    db = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)

# ---- Helper Functions ----
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def split_and_embed(text):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]

    global db
    db = Chroma.from_documents(docs, embedding=embedding_model, persist_directory=persist_directory)
    db.persist()

def handle_question(query):
    if db is None:
        return "❗ No document uploaded yet."
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    return qa_chain.run(query)

# ---- Streamlit UI ----
st.title("PDF Chatbot (Local LLM + Embeddings)")
st.write("Upload a PDF and ask questions about its content.")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    text = read_pdf(uploaded_file)
    st.success("File uploaded. Embedding content...")
    split_and_embed(text)
    st.info("Text embedded. You can now ask questions!")

query = st.text_input("Ask a question:")
if query:
    answer = handle_question(query)
    st.write("Answer: ", answer)
