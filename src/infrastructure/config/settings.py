from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ALLOWED_TOKENS: list[str] = ["token1", "token2"]  # In prod, use env vars
    API_V1_STR: str = "/api/v1"

settings = Settings()