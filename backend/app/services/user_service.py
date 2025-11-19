from app.models.user import User
from app.core.security import hash_password
from sqlalchemy.orm import Session

def create_user(db: Session, username: str, email: str, password: str):
    user = User(username=username, email=email, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
