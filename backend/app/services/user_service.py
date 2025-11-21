from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.crud.crud_user import crud_user
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User


def hash_password(password: str) -> str:
    """
    Hash password using bcrypt safely.
    Ensures password is at most 72 bytes after UTF-8 encoding.
    """
    password_bytes = password.encode("utf-8")
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]  # truncate to 72 bytes
    return bcrypt.hash(password_bytes)


class UserService:
    def get_user(self, db: Session, user_id: int) -> Optional[User]:
        return crud_user.get(db, user_id)

    def get_all_users(self, db: Session) -> List[User]:
        return crud_user.get_all(db)

    def create_user(self, db: Session, user_in: UserCreate) -> User:
        data = user_in.model_dump()
        # Hash password
        if "password" in data:
            data["password"] = hash_password(data["password"])
        # Add timestamps
        data["created_at"] = datetime.now(timezone.utc)
        data["updated_at"] = datetime.now(timezone.utc)
        return crud_user.create(db=db, obj_in=data)

    def update_user(self, db: Session, user_id: int, user_in: UserUpdate) -> Optional[User]:
        db_obj = crud_user.get(db, user_id)
        if not db_obj:
            return None
        updates = user_in.model_dump(exclude_unset=True)
        # Hash password if it is being updated
        if "password" in updates:
            updates["password"] = hash_password(updates["password"])
        updates["updated_at"] = datetime.now(timezone.utc)
        return crud_user.update(db=db, db_obj=db_obj, obj_in=updates)

    def delete_user(self, db: Session, user_id: int) -> bool:
        return crud_user.delete(db, user_id=user_id)


user_service = UserService()
