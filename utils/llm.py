from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )
    return llm


def generate_answer(prompt):
    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content