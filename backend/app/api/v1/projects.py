from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from typing import List

from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate

from app.services.project_service import (
    create_project_service,
    get_project_service,
    update_project_service,
    delete_project_service,
    list_projects_service,
)
from app.db.session import get_db

router = APIRouter( prefix="/projects", tags=["projects"])

@router.post("/", response_model=ProjectRead)

def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project_service(db, project)

@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project_service(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=ProjectRead)
def update_project(project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)):
    db_obj = get_project_service(db, project_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return update_project_service(db, db_obj, project)

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    deleted = delete_project_service(db, project_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"detail": "Project deleted"}

@router.get("/", response_model=List[ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    return list_projects_service(db)