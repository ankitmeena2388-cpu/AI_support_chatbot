from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
def get_response(question: str):

    # Load embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load FAISS DB
    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Search relevant chunks
    docs = db.similarity_search(question, k=3)

    # ✅ CLEAN TEXT OUTPUT (IMPORTANT FIX)
    response = ""
    for doc in docs:
        text = doc.page_content.replace("\n", " ")  # remove broken lines
        response += text + " "

    return response.strip()