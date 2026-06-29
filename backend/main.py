from fastapi import FastAPI
from dotenv import load_dotenv
import asyncio
from langchain_anthropic import ChatAnthropic

load_dotenv()
anthropic = ChatAnthropic(model="claude-haiku-4-5")
app = FastAPI()

@app.get("/")
async def root():
    response = anthropic.invoke("Hello, how are you?")
    return {"message": response}