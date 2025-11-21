from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    Date,
    DateTime,
    Float,
    Enum as PgEnum,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base
import enum


class TaskStatus(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    review = "review"
    done = "done"


class TaskPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)

    # Parent/child relationship
    parent_id = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    children = relationship(
        "Task",
        backref="parent",
        cascade="all, delete-orphan",
        single_parent=True,
        remote_side=[id],
    )

    # Project relation
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)
    project = relationship("Project", back_populates="tasks")

    # Assignments and creators
    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    assignee = relationship(
        "User", back_populates="tasks_assigned", foreign_keys=[assignee_id]
    )

    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    creator = relationship(
        "User", back_populates="tasks_created", foreign_keys=[created_by]
    )

    # Time and estimate
    expected_hours = Column(Float, nullable=True)
    actual_hours = Column(Float, nullable=True)

    # Priority & status
    priority = Column(PgEnum(TaskPriority), nullable=False, server_default=TaskPriority.medium.value)
    status = Column(PgEnum(TaskStatus), nullable=False, server_default=TaskStatus.todo.value)

    due_date = Column(Date, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
