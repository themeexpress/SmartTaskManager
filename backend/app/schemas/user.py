from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: str = "user"  # "admin" | "user"

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None

class UserRead(UserBase):
    id: int
    role: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
