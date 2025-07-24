from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Task Manager API"  # Application name
    debug: bool = True  # Debug mode enabled
    database_url: str  # Database connection URL
    secret_key: str  # JWT signing secret key

    class Config:
        env_file = ".env"  # Load environment variables from .env file


settings = Settings()
