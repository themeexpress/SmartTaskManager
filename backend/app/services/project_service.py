from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy.orm import Session
from app.crud.crud_project import crud_project
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.models.project import Project

class ProjectService:
    def get_project(self, db: Session, project_id: int) -> Optional[Project]:
        return crud_project.get(db, project_id)

    def get_all_projects(self, db: Session) -> List[Project]:
        return crud_project.get_all(db)

    def create_project(self, db: Session, project_in: ProjectCreate) -> Project:
        data = project_in.model_dump()
        # add timestamps if you want
        data["created_at"] = datetime.now(timezone.utc)
        data["updated_at"] = datetime.now(timezone.utc)
        return crud_project.create(db=db, obj_in=ProjectCreate(**data))

    def update_project(self, db: Session, project_id: int, project_in: ProjectUpdate) -> Optional[Project]:
        db_obj = crud_project.get(db, project_id)
        if not db_obj:
            return None
        updates = project_in.model_dump(exclude_unset=True)
        updates["updated_at"] = datetime.now(timezone.utc)
        return crud_project.update(db=db, db_obj=db_obj, obj_in=ProjectUpdate(**updates))

    def delete_project(self, db: Session, project_id: int) -> bool:
        return crud_project.delete(db, project_id=project_id)

project_service = ProjectService()
