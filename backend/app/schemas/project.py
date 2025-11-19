from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class ProjectUpdate(BaseModel):
    name: str 
    description: Optional[str] = None
