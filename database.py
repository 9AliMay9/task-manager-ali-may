from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


SQLALCHEMY_DATABASE_URL = settings.database_url


# Create SQLAlchemy engine using the database URL from config
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get a DB session for each request
def get_db():
    """
    Provides a database session to route functions.
    Ensures session is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
