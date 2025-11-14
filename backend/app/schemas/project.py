from pydantic import BaseModel, EmailStr


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None


class ProjectRead(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        orm_mode = True
