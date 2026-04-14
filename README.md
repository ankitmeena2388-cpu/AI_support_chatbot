# 🤖 AI Customer Support Chatbot API

A FastAPI-based AI chatbot that allows users to upload PDF documents and ask questions based on the content.  
This project uses LangChain, FAISS, and HuggingFace embeddings to perform semantic search and provide intelligent answers.

---

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Extract and process text from PDFs
- 🧠 Create vector embeddings using HuggingFace
- ⚡ Store embeddings using FAISS
- 💬 Ask questions based on uploaded PDF
- ⚙️ FastAPI backend with interactive Swagger UI

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **AI Framework:** LangChain
- **Embeddings:** HuggingFace (MiniLM)
- **Vector DB:** FAISS
- **PDF Processing:** PyPDF
- **Server:** Uvicorn

---

## 📂 Project Structure

p_1/
│── app/
│ ├── main.py
│ ├── chatbot.py
│ └── vectorstore.py
│
│── data/ # Uploaded PDFs
│── faiss_index/ # Vector database (auto-generated)
│── venv/ # Virtual environment (ignored)
│── .gitignore
│── README.md



---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/chatbot-api.git
cd chatbot-api


python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt
If requirements.txt is not available:
pip install fastapi uvicorn langchain langchain-community langchain-huggingface faiss-cpu pypdf

▶️ Run the Project
python -m uvicorn app.main:app --reload

🌐 API Endpoints
🔹 1. Home
GET /

🔹 2. Upload PDF
POST /upload


Upload a PDF file


Creates vector database



🔹 3. Ask Question
POST /ask
Request Body:
{  "question": "What is customer service automation?"}
Response:
{  "response": "AI-driven customer service automation uses..."}

🧪 Testing (Swagger UI)
Open in browser:
http://127.0.0.1:8000/docs

⚠️ Notes


Upload PDF before asking questions


faiss_index/ is auto-generated


venv/ is ignored using .gitignore



📌 Future Improvements


🌐 Deploy on cloud (Render / AWS)


🧾 Support multiple PDFs


💡 Improve answer formatting


🔐 Add authentication


🗣️ Voice-based interaction



👨‍💻 Author
Ankit Meena

