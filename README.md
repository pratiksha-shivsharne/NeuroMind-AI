# NeuroMind AI 🧠 - RAG Chatbot for PDF Q&A

Upload any PDF and ask questions in plain English. NeuroMind AI finds the relevant parts of the document and gives answers based on its content.

## How it works
1. PDF text is extracted and split into chunks (LangChain)
2. Chunks are converted to embeddings (HuggingFace)
3. Semantic search finds the best matching chunks (FAISS / ChromaDB)
4. Retrieved context is sent to Llama 3.3 70B (via Groq) to generate a grounded answer, which reduces hallucination

## Tech Stack
Python, LangChain, FAISS / ChromaDB, HuggingFace Embeddings, Llama 3.3 70B (Groq), FastAPI, Streamlit, Docker, AWS EC2

## Deployment
The app is containerized with Docker and deployed on an AWS EC2 instance (Streamlit frontend + FastAPI backend).

## Screenshot
![NeuroMind AI](screenshot.png)

## Author
Pratiksha Shivsharne - [LinkedIn](https://www.linkedin.com/in/pratiksha-shivsharne)
