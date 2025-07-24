from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskBase(BaseModel):
    """
    Base schema for a task. Contains shared fields.
    """
    title: str                              # Task title
    description: Optional[str] = None       # Optional task description
    completed: Optional[bool] = False       # Task completion status


class TaskCreate(TaskBase):
    """
    Schema used when creating a new task.
    """
    pass # Inherits all fields from TaskBase


class TaskUpdate(BaseModel):
    """
    Schema used when updating an existing task.
    """
    title: Optional[str] = None             # New title (optional)
    description: Optional[str] = None       # New description (optional)
    completed: Optional[bool] = None        # Updated completion status


class TaskOut(TaskBase):
    """
    Schema used when returning a task from the API.
    """
    id: int                                 # Unique task ID
    created_at: datetime                    # Creation timestamp
    updated_at: Optional[datetime] = None   # Last update timestamp


    class Config:
        from_attributes = True # Enable ORM mode to allow reading from SQLAlchemy models
