import streamlit as st
import sys
import os

# ----------------------------
# Project Path
# ----------------------------
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

# ----------------------------
# Imports
# ----------------------------
from utils.pdf_reader import extract_text_from_pdf
from utils.text_chunker import split_text
from utils.vector_store import create_vector_store
from utils.retriever import get_relevant_chunks
from utils.prompt import build_prompt
from utils.llm import generate_answer

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="NeuroMind AI",
    page_icon="🧠",
    layout="wide"
)

# ----------------------------
# Session State
# ----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------
# Title
# ----------------------------
st.title("🧠 NeuroMind AI")
st.markdown("### 📄 Chat with your PDF using AI")

st.divider()

# ----------------------------
# Upload PDF
# ----------------------------
uploaded_file = st.file_uploader(
    "Upload a PDF File",
    type=["pdf"]
)

# ----------------------------
# Ask Question
# ----------------------------
question = st.text_input(
    "Ask a Question",
    placeholder="Example: Summarize this PDF"
)

# ----------------------------
# Ask AI
# ----------------------------
if st.button("🚀 Ask AI"):

    if uploaded_file is None:
        st.warning("⚠️ Please upload a PDF first.")
        st.stop()

    if question.strip() == "":
        st.warning("⚠️ Please enter a question.")
        st.stop()

    # ----------------------------
    # Read PDF
    # ----------------------------
    with st.spinner("📄 Reading PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    st.success("✅ PDF Read Successfully")

    if len(pdf_text) == 0:
        st.error("❌ No text found in PDF.")
        st.stop()

    # ----------------------------
    # Split Text
    # ----------------------------
    with st.spinner("✂️ Creating Chunks..."):
        chunks = split_text(pdf_text)

    st.success(f"✅ {len(chunks)} Chunks Created")

    if len(chunks) == 0:
        st.error("❌ No chunks created.")
        st.stop()

    # ----------------------------
    # Create FAISS Index
    # ----------------------------
    with st.spinner("🧠 Creating FAISS Index..."):
        create_vector_store(chunks)

    st.success("✅ FAISS Index Created")

    # ----------------------------
    # Retrieve Relevant Chunks
    # ----------------------------
    with st.spinner("🔍 Searching Relevant Chunks..."):
        docs = get_relevant_chunks(question)

    st.success(f"✅ Retrieved {len(docs)} Relevant Chunks")

    # ----------------------------
    # Build Context
    # ----------------------------
    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    # ----------------------------
    # Build Prompt
    # ----------------------------
    prompt = build_prompt(context, question)

    st.success("✅ Prompt Created")

    # ----------------------------
    # Generate AI Answer
    # ----------------------------
    with st.spinner("🤖 Generating Answer..."):
        answer = generate_answer(prompt)

    st.success("✅ Answer Generated")

    # ----------------------------
    # Save Chat History
    # ----------------------------
    st.session_state.chat_history.append(
        {
            "question": question,
            "answer": answer
        }
    )

    # ----------------------------
    # Final Answer
    # ----------------------------
    st.write("## 🤖 AI Answer")
    st.success(answer)

    # ----------------------------
    # Source Citations
    # ----------------------------
    st.write("## 📖 Sources Used")

    if docs:

        for i, doc in enumerate(docs, start=1):

            with st.expander(f"📄 Source {i}"):

                st.write(doc.page_content)

    else:

        st.warning("No source chunks found.")

    # ----------------------------
    # PDF Preview
    # ----------------------------
    with st.expander("📄 PDF Preview"):
        st.text(pdf_text[:1000])

# ----------------------------
# Chat History
# ----------------------------
st.divider()

st.subheader("💬 Chat History")

if len(st.session_state.chat_history) == 0:
    st.info("No chat history yet.")

else:

    for i, chat in enumerate(st.session_state.chat_history, start=1):

        st.markdown(f"### Conversation {i}")

        st.markdown("**👤 You:**")
        st.write(chat["question"])

        st.markdown("**🤖 AI:**")
        st.success(chat["answer"])

        st.divider()

# ----------------------------
# Clear Chat Button
# ----------------------------
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.success("✅ Chat history cleared successfully!")
    st.rerun()