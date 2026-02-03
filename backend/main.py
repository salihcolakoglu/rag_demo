from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import fitz  # PyMuPDF

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"reply": f"echo: {req.message}"}

@app.post("/documents")
async def upload_document(file: UploadFile = File(...)):
    pdf_bytes = await file.read()

    # PyMuPDF ile metin çıkar
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    texts = []
    for i in range(len(doc)):
        t = doc[i].get_text("text") or ""
        texts.append(t)

    num_pages = len(texts)
    full_text = "\n".join(texts)
    char_count = len(full_text)

    # Preview: ilk dolu sayfadan 300 karakter
    preview = ""
    for t in texts:
        if t.strip():
            preview = t[:300]
            break

    return {
        "filename": file.filename,
        "num_pages": num_pages,
        "char_count": char_count,
        "text_preview": preview
    }
