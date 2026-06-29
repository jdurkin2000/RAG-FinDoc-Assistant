from pathlib import Path

import fitz
import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

ollama_embeddings = OllamaEmbeddings(model="nomic-embed-text")
chroma_client = Chroma(
    collection_name="financial_documents",
    embedding_function=ollama_embeddings,
    persist_directory="backend/data/chroma"
    )
    

def _get_text_splitter(
    *,
    chunk_size: int = CHUNK_SIZE,
    chunk_overlap: int = CHUNK_OVERLAP,
) -> RecursiveCharacterTextSplitter:
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True
    )

def load_pdf(pdf_path: str | Path) -> Document:
    path = Path(pdf_path)
    doc = fitz.open(path)
    try:
        pages = [page.get_text() for page in doc]
    finally:
        doc.close()
    text = "\n".join(pages)
    return Document(page_content=text, metadata={"source": str(path)})

def add_chunks_to_chroma(chunks: list[Document]) -> list[str]:
    return chroma_client.add_documents(documents=chunks)

def ingest_documents(directory: str | Path) -> list[str]:
    documents = [load_pdf(file) for file in Path(directory).glob("*.pdf")]
    chunked = _get_text_splitter().split_documents(documents)
    return add_chunks_to_chroma(chunked)

print("Loading documents into Chroma...")
print(ingest_documents("backend/data/financial_documents"))
print("Documents loaded into Chroma")
