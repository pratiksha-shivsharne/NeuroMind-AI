import streamlit as st

import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from utils.pdf_reader import extract_text_from_pdf
# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="NeuroMind AI",
    page_icon="🧠",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("🧠 NeuroMind AI")
st.markdown("### 📄 Chat with your PDF using AI")

st.divider()

# ----------------------------
# PDF Upload
# ----------------------------
uploaded_file = st.file_uploader(
    "Upload a PDF File",
    type=["pdf"]
)

# ----------------------------
# Question Input
# ----------------------------
question = st.text_input(
    "Ask a Question",
    placeholder="Example: Summarize this PDF"
)

# ----------------------------
# Button
# ----------------------------
if st.button("🚀 Ask AI"):

    if uploaded_file is None:
        st.warning("Please upload a PDF first.")

    elif question == "":
        st.warning("Please enter your question.")

    else:

        pdf_text = extract_text_from_pdf(uploaded_file)

        st.success("PDF Read Successfully!")

        st.write("### Extracted Text")

        st.text(pdf_text[:1000])