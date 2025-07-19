from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Task Manager API"         # Application name
    debug: bool = True                         # Enable debug mode
    database_url: str = "sqlite:///./task.db"  # Default to SQLite local file database


    class Config:
        env_file = ".env"  # Load variables from .env file if it exists


# Instantiate the settings object for global config access
settings = Settings()
