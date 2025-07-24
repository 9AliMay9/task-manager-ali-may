from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


# Load database URL from config
SQLALCHEMY_DATABASE_URL = settings.database_url


# Initialize the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency: provide a database session per request
def get_db():
    """
    Yield a database session.
    Ensures the session is closed after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
