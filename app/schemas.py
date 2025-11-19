from datetime import date
from pydantic import BaseModel

class TodoSchema(BaseModel):
    id: int
    task: str
    completed: bool
    due_date: date | None
    created_at: date

class TodoCreateSchema(BaseModel):
    task: str
    completed: bool = False
    due_date: date | None = None

class TodoUpdateSchema(BaseModel):
    task: str | None = None
    completed: bool | None = None
    due_date: date | None = None