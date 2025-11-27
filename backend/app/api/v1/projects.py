from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.services.project_service import project_service
from app.db.session import get_db

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=ProjectRead)
def create_project(project_in: ProjectCreate, db: Session = Depends(get_db)):
    return project_service.create_project(db=db, project_in=project_in)

@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = project_service.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project

@router.get("/", response_model=List[ProjectRead])
def get_projects(db: Session = Depends(get_db)):
    return project_service.get_all_projects(db)

@router.put("/{project_id}", response_model=ProjectRead)
def update_project(project_id: int, project_in: ProjectUpdate, db: Session = Depends(get_db)):
    updated = project_service.update_project(db, project_id, project_in)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return updated

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    deleted = project_service.delete_project(db, project_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return {"detail": "Project deleted successfully"}
