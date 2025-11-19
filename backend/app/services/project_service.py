from sqlalchemy.orm import Session
from app.crud.crud_project import crud_project
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.models.project import Project


def create_project_service(db: Session, project: ProjectCreate) -> Project:
    return crud_project.create(db, obj_in=project)

def get_project_service(db: Session, project_id: int):
    return crud_project.get(db, project_id=project_id)

def update_project_service(db: Session, db_obj, project: ProjectUpdate):
    return crud_project.update(db, db_obj=db_obj, obj_in=project)

def delete_project_service(db: Session, project_id: int):
    return crud_project.delete(db, project_id=project_id)

def list_projects_service(db: Session):
    return crud_project.get_all(db)