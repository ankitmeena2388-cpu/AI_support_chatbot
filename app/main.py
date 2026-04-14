from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from app.vectorstore import create_vector_store
from app.chatbot import get_response

app = FastAPI(
    title="AI Customer Support Chatbot API",
    version="1.0.0",
    description="Upload PDF and ask questions from it"
)

# Request model
class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "API is running successfully 🚀"}


# ✅ Upload PDF
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        os.makedirs("data", exist_ok=True)

        file_path = f"data/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Create vector DB
        create_vector_store(file_path)

        return {"message": "PDF uploaded and processed successfully ✅"}

    except Exception as e:
        return {"error": str(e)}


# ✅ Ask Question
@app.post("/ask")
def ask_question(query: Query):
    try:
        answer = get_response(query.question)

        return {
            "question": query.question,
            "answer": answer
        }

    except Exception as e:
        return {"error": str(e)}