from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    description: Optional[str]


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    created_at: datetime
    tasks: List['Task'] = []

    class Config:
        from_attributes = True
