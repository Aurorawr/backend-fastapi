from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"  # Valor por defecto si no está en el .env
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 # Valor por defecto si no está en el .env

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8"
    )

settings = Settings()