from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str]
    deadline: datetime
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    user_id: int
    project_id: int
    priority_id: int


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    created_at: datetime
    owner: 'User'
    project: 'Project'
    priority: 'Priority'
    categories: List['Category']

    class Config:
        from_attributes = True

    class Config:
        orm_mode = True
