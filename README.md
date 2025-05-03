# local-llm-pdf-chatbot
A local LLM-powered chatbot built using Python, Ollama, ChromaDB, and Streamlit. Upload your PDFs and ask questions — all processed locally with privacy and speed.


# Local LLM PDF Chatbot

A **local PDF chatbot** built using **Python**, **Ollama**, **LangChain**, **ChromaDB**, and **Streamlit**. Upload a PDF or text file, and interact with it by asking questions — all processed **locally** using a small LLM model.

---

## Features

- ✅ Upload and read PDFs
- ✅ Store embeddings using ChromaDB locally
- ✅ Use Ollama for running lightweight local LLMs
- ✅ Ask questions and get answers from the uploaded document
- ✅ No OpenAI API key required — everything runs locally (except embeddings if OpenAI is used)

---

##  Tech Stack

| Tool              | Purpose                                 |
|------------------|-----------------------------------------|
| Python           | Core Programming Language               |
| Streamlit        | Simple web UI                           |
| Ollama           | Local LLM runner (e.g., `tinyllama`)    |
| ChromaDB         | Vector database to store document embeddings |
| LangChain        | Integration between models and retrievers |
| PyPDF2           | PDF text extraction                     |
| dotenv           | Environment variable management         |

---

## Installation

2. clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/local-llm-pdf-chatbot.git
cd local-llm-pdf-chatbot


2. Set up your environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

3. Install and run Ollama
After installing Ollama -
ollama serve
ollama pull tinyllama ( you can change model here like mistral)
check the model configuration as per your System.

Optional (OpenAI Embeddings) - We are using HuggingFaceEmbeddings in this project
OPENAI_API_KEY=your_openai_key ( add this in .env file)
