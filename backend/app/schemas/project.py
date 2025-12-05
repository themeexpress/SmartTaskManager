from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

class ProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=250)
    description: Optional[str] = Field(None, max_length=2000)

class ProjectCreate(ProjectBase):
    owner_id: int

class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(..., min_length=1, max_length=250)
    description: Optional[str] = Field(None, max_length=2000)

class ProjectRead(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
