\# RAG Demo (FastAPI + Streamlit)



\## Structure

\- backend/ : FastAPI API (health, chat, documents upload)

\- frontend/: Streamlit UI (PDF upload + preview)



\## Setup (Windows)

\### Backend

```powershell

conda create -n rag-backend python=3.11 -y

conda activate rag-backend

pip install -r backend/requirements.txt

cd backend

uvicorn main:app --reload --port 8000
