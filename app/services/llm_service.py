from langchain_anthropic import ChatAnthropic
from app.config import settings

client = ChatAnthropic(model=settings.llm_model, api_key=settings.anthropic_api_key)

def query_llm(message: str) -> str:
    response = client.invoke(message)
    return response.content