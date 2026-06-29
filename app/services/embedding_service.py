from langchain_ollama import OllamaEmbeddings
from app.config import settings

embedding_func = OllamaEmbeddings(model=settings.embedding_model)