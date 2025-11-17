from datetime import date

from sqlalchemy import Date, Integer, String, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task: Mapped[str]  = mapped_column(String(255), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    due_date: Mapped[date] = mapped_column(Date)
    created_at: Mapped[date] = mapped_column(Date, server_default=func.date('now'))