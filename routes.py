from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Task
from schemas import TaskCreate, TaskOut, TaskUpdate
import crud


router = APIRouter()


@router.post("/tasks/", response_model=TaskOut)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.
    """
    return crud.create_task(db, task_data)


@router.get("/tasks/", response_model=list[TaskOut])
def read_all_tasks(db: Session = Depends(get_db)):
    """
    Retrieve all tasks.
    """
    return crud.get_all_tasks(db)


@router.get("/tasks/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a task by ID.
    """
    task = crud.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    """
    Update an existing task by ID.
    """
    updated_task = crud.update_task(db, task_id, task_data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task by ID.
    """
    success = crud.delete_task_by_id(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}
