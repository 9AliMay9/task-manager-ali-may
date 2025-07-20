from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate


def create_task(db: Session, task_data: TaskCreate) -> Task:
    """
    Create a new task in the database.
    """
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed,
        )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_task_by_id(db: Session, task_id: int) -> Task | None:
    """
    Retrieve a task by its ID.
    """
    return db.query(Task).filter(Task.id == task_id).first()


def get_all_tasks(db: Session) -> list[Task]:
    """
    Retrieve all tasks from the database.
    """
    return db.query(Task).all()


def update_task(db: Session, task_id: int, task_data: TaskUpdate) -> Task | None:
    """
    Update an existing task by its ID.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed
    db.commit()
    db.refresh(task)
    return task


def delete_task_by_id(db: Session, task_id: int) -> bool:
    """
    Delete a task by its ID.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True
