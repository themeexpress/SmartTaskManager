from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional, List, Union
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class CRUDTask:
    def get(self, db: Session, task_id: int) -> Optional[Task]:
        return db.query(Task).filter(Task.id == task_id).first()

    def get_all(self, db: Session) -> List[Task]:
        return db.query(Task).all()

    def create(self, db: Session, *, obj_in: Union[TaskCreate, dict]) -> Task:
        try:
            if isinstance(obj_in, dict):
                data = obj_in
            else:
                data = obj_in.model_dump()
            
            db_obj = Task(**data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def update(self, db: Session, *, db_obj: Task, obj_in: dict) -> Task:
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, task_id: int) -> bool:
        db_obj = self.get(db, task_id)
        if not db_obj:
            return False
        db.delete(db_obj)
        db.commit()
        return True


crud_task = CRUDTask()
