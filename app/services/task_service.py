from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def get_all_tasks(db: Session):
    return db.query(Task).all()


def get_task_or_404(db: Session, task_id: int) -> Task:
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


def create_task(db: Session, task_data: TaskCreate) -> Task:
    task = Task(**task_data.model_dump())

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def update_task(
    db: Session,
    task_id: int,
    task_data: TaskCreate,
) -> Task:
    task = get_task_or_404(db, task_id)

    for field, value in task_data.model_dump().items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task_id: int) -> None:
    task = get_task_or_404(db, task_id)

    db.delete(task)
    db.commit()


def patch_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate,
) -> Task:
    task = get_task_or_404(db, task_id)

    update_data = task_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task
