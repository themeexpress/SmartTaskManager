from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead
from app.core.deps import get_db
from app.services.user_service import create_user, get_user_by_email
from app.core.security import create_access_token, verify_password

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post("/register", response_model=UserRead)
def register(u: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, u.email):
        raise HTTPException(400, "Email already registered")
    return create_user(db, u.username, u.email, u.password)

@router.post("/login")
def login(form_data: UserCreate, db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.email)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(401, "Invalid credentials")
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}
