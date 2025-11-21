# app/api/v1/tasks.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskRead
from app.services.task_service import task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.get("/", response_model=list[TaskRead])
def get_all_tasks(db: Session = Depends(get_db)):
    return task_service.get_all_tasks(db)


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task_in)


@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_in: TaskUpdate, db: Session = Depends(get_db)):
    updated = task_service.update_task(db, task_id, task_in)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    success = task_service.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
