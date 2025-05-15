from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
