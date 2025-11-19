from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from typing import Optional, List

class CRUDProject:
    def get(self, db: Session, project_id: int) -> Optional[Project]:
        return db.query(Project).filter(Project.id == project_id).first()

    def get_all(self, db: Session) -> List[Project]:
        return db.query(Project).all()

    def create(self, db: Session, *, obj_in: ProjectCreate) -> Project:
        db_obj = Project(
            name=obj_in.name,
            description=obj_in.description
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: Project, obj_in: ProjectUpdate) -> Optional[Project]:
        obj_data = self.get(db, project_id=db_obj.id)
        if not obj_data:
            return None
        
        db_obj.name = obj_in.name
        db_obj.description = obj_in.description
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, project_id: int) -> bool:
        db_obj = self.get(db, project_id)
        if not db_obj:
            return False
        
        db.delete(db_obj)
        db.commit()
        return True
    

crud_project = CRUDProject()
