from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
from anthropic import AsyncAnthropic
import os
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield

anthropic = AsyncAnthropic(api_key=os.getenv("CLAUDE_API_KEY"))
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    response = await anthropic.messages.create(
        model="claude-haiku-4-5",
        messages=[
            {
                "role": "user",
                "content": "Hello, how are you?"
            }
        ],
        max_tokens=1000
    )
    return {"message": response.content[0].text}