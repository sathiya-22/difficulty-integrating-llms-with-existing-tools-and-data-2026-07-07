import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    api_key: SecretStr = Field(..., env="GEMINI_API_KEY")
    wayflow_url: str = Field(..., env="WAYFLOW_URL")

settings = Settings()
