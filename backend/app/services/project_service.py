from sqlalchemy.orm import Session
from app.crud.crud_project import crud_project
from app.schemas.project import ProjectCreate, ProjectUpdate
from typing import List, Optional
from app.models.project import Project

class ProjectService:
    def get_project(self, db: Session, project_id: int) -> Optional[Project]:
        return crud_project.get(db, project_id)

    def get_projects(self, db: Session) -> List[Project]:
        return crud_project.get_all(db)

    def create_project(self, db: Session, project_in: ProjectCreate) -> Project:
        return crud_project.create(db, obj_in=project_in)

    def update_project(self, db: Session, project_id: int, project_in: ProjectUpdate) -> Optional[Project]:
        db_obj = crud_project.get(db, project_id)
        if not db_obj:
            return None
        return crud_project.update(db, db_obj=db_obj, obj_in=project_in)

    def delete_project(self, db: Session, project_id: int) -> bool:
        return crud_project.delete(db, project_id=project_id)

project_service = ProjectService()
