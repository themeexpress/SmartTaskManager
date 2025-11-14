from sqlalchemy import Column, Integer, String,Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from backend.app.db.session import Base
import enum

class TaskStatus(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed" 
    cancelled = "cancelled"


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(String, default=True)
    
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING, nullable=False)
    due_date = Column(Date, nullable=True)
    
    assignee_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    
    assignee = relationship("User")
    project = relationship("Project")