from database import engine
from models import Base

# Create all tables defined in the models using the SQLAlchemy engine
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
