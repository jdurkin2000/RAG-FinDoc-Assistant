from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Personal FinDoc Assistant"
    vector_collection_name: str = "financial_documents"

    anthropic_api_key: str
    llm_model: str
    chroma_url: str = "data/chroma"

    embedding_model: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()