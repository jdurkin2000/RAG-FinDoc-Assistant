from .config import settings
from fastapi import FastAPI
from .services.llm_service import query_llm

app = FastAPI(title=settings.app_name)

@app.get("/")
async def root():
    return query_llm("Hello, how are you?")