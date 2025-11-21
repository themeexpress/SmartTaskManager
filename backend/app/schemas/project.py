from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    created_by: int  # user_id who created the project

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class ProjectRead(ProjectBase):
    id: int
    created_by: int

    model_config = ConfigDict(from_attributes=True)
