from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date, datetime
from app.models.task import TaskStatus, TaskPriority

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=250)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[TaskStatus] = TaskStatus.todo
    priority: Optional[TaskPriority] = TaskPriority.medium
    due_date: Optional[date] = None
    expected_hours: Optional[float] = Field(None, ge=0)
    actual_hours: Optional[float] = Field(None, ge=0)
    parent_id: Optional[int] = None
    assignee_id: Optional[int] = None
    project_id: Optional[int] = None

class TaskCreate(TaskBase):
    model_config = ConfigDict(extra="forbid")  # block client from sending created_by

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=250)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[date] = None
    expected_hours: Optional[float] = Field(None, ge=0)
    actual_hours: Optional[float] = Field(None, ge=0)
    parent_id: Optional[int] = None
    assignee_id: Optional[int] = None
    project_id: Optional[int] = None

    model_config = ConfigDict(extra="forbid")

class TaskRead(TaskBase):
    id: int
    created_by: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
