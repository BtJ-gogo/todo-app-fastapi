from datetime import date

from sqlalchemy import Date, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    task: Mapped[str]  = mapped_column()
    completed: Mapped[bool] = mapped_column(default=False)
    due_date: Mapped[date] = mapped_column(Date)
    created_at: Mapped[date] = mapped_column(Date, server_default=func.date('now'))