from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id")) # Foreign key to User.id can be added later
    owner = relationship("User")