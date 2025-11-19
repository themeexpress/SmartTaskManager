from pydantic import BaseModel, ConfigDict
from datetime import date
from app.models.task import TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.pending
    priority: str | None = "medium"
    due_date: date | None = None
    assignee_id: int | None = None
    project_id: int | None = None


class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    priority: str | None = None
    status: TaskStatus
    due_date: date | None = None
    assignee_id: int | None = None
    project_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
