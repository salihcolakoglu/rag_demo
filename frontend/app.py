import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="RAG Demo", layout="centered")
st.title("PDF Doküman Asistanı (RAG Demo)")

st.caption("Bugün: PDF upload + metin çıkarma önizleme. Sonra: chunking + arama + kaynaklı cevap.")

uploaded = st.file_uploader("PDF yükle", type=["pdf"])

if uploaded is not None:
    try:
        pdf_bytes = uploaded.getvalue()

        r = requests.post(
            f"{API_URL}/documents",
            files={"file": (uploaded.name, pdf_bytes, "application/pdf")},
            timeout=120
        )
        r.raise_for_status()
        info = r.json()

        st.success("PDF backend'e yüklendi ✅")
        st.write("Dosya:", info.get("filename"))
        st.write("Sayfa sayısı:", info.get("num_pages"))
        st.write("Karakter sayısı:", info.get("char_count"))

        st.text_area(
            "Metin önizleme (ilk 300 karakter)",
            info.get("text_preview", ""),
            height=180
        )

    except Exception as e:
        st.error(f"PDF upload hatası: {e}")
