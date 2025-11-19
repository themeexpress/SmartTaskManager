from pydantic import BaseModel, ConfigDict, EmailStr


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None


class ProjectRead(BaseModel):
    id: int
    name: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)
