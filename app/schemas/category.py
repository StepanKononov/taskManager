from typing import List, Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: Optional[str]


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    tasks: List['Task'] = []

    class Config:
        from_attributes = True
