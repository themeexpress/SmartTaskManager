from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy.orm import Session
#from passlib.hash import bcrypt
from app.crud.crud_user import crud_user
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User


import bcrypt as _bcrypt

from app.core.exceptions import NotFoundException

def hash_password(pw: str) -> str:
    b = pw.encode('utf-8')[:72]   # always ≤ 72 bytes
    return _bcrypt.hashpw(b, _bcrypt.gensalt()).decode()


class UserService:
    def get_user(self, db: Session, user_id: int) -> Optional[User]:
        return crud_user.get(db, user_id)

    def get_all_users(self, db: Session) -> List[User]:
        return crud_user.get_all(db)

    def create_user(self, db: Session, user_in: UserCreate) -> User:
        data = user_in.model_dump()
        # Hash password
        if "password" in data:
            print("RAW PASSWORD RECEIVED:", repr(data["password"])) 
            data["password"] = hash_password(data["password"])
        # Add timestamps
        data["created_at"] = datetime.now(timezone.utc)
        data["updated_at"] = datetime.now(timezone.utc)
        
        obj = UserCreate(**data)

        return crud_user.create(db=db, obj_in=obj)

    def update_user(self, db: Session, user_id: int, user_in: UserUpdate) -> Optional[User]:
        db_obj = crud_user.get(db, user_id)
        if not db_obj:
            raise NotFoundException("Task not found")
        updates = user_in.model_dump(exclude_unset=True)
        # Hash password if it is being updated
        if "password" in updates:
            print("RAW PASSWORD RECEIVED:", repr(data["password"])) 
            updates["password"] = hash_password(updates["password"])
        updates["updated_at"] = datetime.now(timezone.utc)
        return crud_user.update(db=db, db_obj=db_obj, obj_in=updates)

    def delete_user(self, db: Session, user_id: int) -> bool:
        return crud_user.delete(db, user_id=user_id)


user_service = UserService()
