from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


# Base class for all ORM models
Base = declarative_base()


class Task(Base):
    """
    ORM model for a task item in the task manager system.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)  # Unique task ID
    title = Column(String(100), nullable=False, index=True)  # Task title
    description = Column(String(250), nullable=True)  # Optional task description
    completed = Column(Boolean, default=False)  # Task completion status
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp on creation
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp on update
