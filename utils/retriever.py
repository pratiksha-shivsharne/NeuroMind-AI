from utils.vector_store import load_vector_store


def get_relevant_chunks(question):
    db = load_vector_store()

    docs = db.similarity_search(
        question,
        k=3
    )

    return docs