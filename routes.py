from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from database import get_db
from models import Task
from schemas import TaskCreate, TaskOut, TaskUpdate
from auth import require_permission
import crud


router = APIRouter(tags=["Tasks"])


@router.post("/", response_model=TaskOut)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.
    """
    return crud.create_task(db, task_data)


@router.get("/", response_model=list[TaskOut])
def read_all_tasks(
        db: Session = Depends(get_db),
        _: dict = Security(require_permission(["read"])),
):
    """
    Get all tasks.
    Requires JWT token with 'read' permission.
    """
    return crud.get_all_tasks(db)


@router.get("/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Get a task by its ID.
    Raises 404 if the task does not exist.
    """
    task = crud.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    """
    Update a task by its ID.
    """
    updated_task = crud.update_task(db, task_id, task_data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/{task_id}", response_model=dict)
def delete_task(
        task_id: int,
        db: Session = Depends(get_db),
        _: dict = Security(require_permission(["delete"])),
):
    """
    Delete a task by its ID.
    Requires JWT token with 'delete' permission.
    """
    success = crud.delete_task_by_id(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}
