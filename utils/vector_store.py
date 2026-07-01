from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embedding_model


def create_vector_store(chunks):
    embedding = get_embedding_model()

    vector_db = FAISS.from_texts(
        texts=chunks,
        embedding=embedding
    )

    # Save FAISS index
    vector_db.save_local("data/faiss_index")

    return vector_db


def load_vector_store():
    embedding = get_embedding_model()

    vector_db = FAISS.load_local(
        "data/faiss_index",
        embedding,
        allow_dangerous_deserialization=True
    )

    return vector_db