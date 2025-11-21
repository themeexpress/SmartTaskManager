from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.user import User
from app.schemas.user import UserCreate, UserRead

class CRUDUser:
    def get(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    def get_all(self, db: Session) -> List[User]:
        return db.query(User).all()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            email=obj_in.email,
            password=obj_in.password  # Note: hash in real app
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, user_id: int) -> bool:
        db_obj = self.get(db, user_id)
        if not db_obj:
            return False
        db.delete(db_obj)
        db.commit()
        return True

crud_user = CRUDUser()