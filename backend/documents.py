from pathlib import Path

import fitz
from langchain_text_splitters import CharacterTextSplitter

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


def _get_text_splitter(
    *,
    chunk_size: int = CHUNK_SIZE,
    chunk_overlap: int = CHUNK_OVERLAP,
) -> CharacterTextSplitter:
    return CharacterTextSplitter.from_tiktoken_encoder(
        separator="",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        encoding_name="cl100k_base"
    )


def extract_text_from_pdf(pdf_path: str | Path) -> str:
    path = Path(pdf_path)
    doc = fitz.open(path)
    try:
        pages = [page.get_text() for page in doc]
    finally:
        doc.close()
    return "\n".join(pages)


def split_text_into_chunks(
    text: str,
    *,
    chunk_size: int = CHUNK_SIZE,
    chunk_overlap: int = CHUNK_OVERLAP,
) -> list[str]:
    if not text.strip():
        return []

    splitter = _get_text_splitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_text(text)


def load_pdf_chunks(
    pdf_path: str | Path,
    *,
    chunk_size: int = CHUNK_SIZE,
    chunk_overlap: int = CHUNK_OVERLAP,
) -> list[str]:
    text = extract_text_from_pdf(pdf_path)
    return split_text_into_chunks(
        text,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

print(load_pdf_chunks("backend/data/test.pdf"))