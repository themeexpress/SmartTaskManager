from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.crud.crud_task import crud_task
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.task import Task
from typing import Optional, List


class TaskService:
    def get_task(self, db: Session, task_id: int) -> Optional[Task]:
        return crud_task.get(db, task_id)

    def get_all_tasks(self, db: Session) -> List[Task]:
        return crud_task.get_all(db)

    def create_task(self, db: Session, task_in: TaskCreate) -> Task:
        # Add timestamps
        data = task_in.model_dump()
        data["created_at"] = datetime.now(timezone.utc)
        data["updated_at"] = datetime.now(timezone.utc)

        return crud_task.create(db=db, obj_in=data)

    def update_task(self, db: Session, task_id: int, task_in: TaskUpdate) -> Optional[Task]:
        db_obj = crud_task.get(db, task_id)
        if not db_obj:
            return None

        updates = task_in.model_dump(exclude_unset=True)
        updates["updated_at"] = datetime.now(timezone.utc)

        return crud_task.update(db=db, db_obj=db_obj, obj_in=updates)

    def delete_task(self, db: Session, task_id: int) -> bool:
        return crud_task.delete(db, task_id=task_id)


task_service = TaskService()
