from app.services.embedding_service import embedding_func
from app.config import settings

from langchain_chroma import Chroma
from langchain_core.documents import Document

vector_db = Chroma(
    collection_name=settings.vector_collection_name,
    embedding_function=embedding_func,
    persist_directory=settings.chroma_url
)