from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional
from app.models.task import TaskStatus, TaskPriority

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
    priority: TaskPriority = TaskPriority.medium
    due_date: Optional[date] = None
    expected_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    parent_id: Optional[int] = None
    assigned_to: Optional[int] = None
    project_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[date] = None
    expected_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    parent_id: Optional[int] = None
    assigned_to: Optional[int] = None
    project_id: Optional[int] = None

class TaskRead(TaskBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
