from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()


def get_llm():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )
    return llm


def build_prompt(context, question):
    prompt = f"""
You are an AI assistant.

Answer the user's question ONLY using the information provided in the context.

If the answer is not available in the context, reply:
"I couldn't find the answer in the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt


def generate_answer(prompt):
    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content