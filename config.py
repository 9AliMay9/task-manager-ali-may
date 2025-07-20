from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application name
    app_name: str = "Task Manager API"

    # Enable debug mode
    debug: bool = True

    # Default to PostgreSQL local file database
    database_url: str

    class Config:
        env_file = ".env"  # Load variables from .env file if it exists


# Instantiate the settings object for global config access
settings = Settings()
