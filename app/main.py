from fastapi import FastAPI, Depends, HTTPException

from app.database import engine, Base, get_db
from app.models import Todo
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import TodoSchema, TodoCreateSchema, TodoUpdateSchema

#  Create the database tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await create_tables()

# List all tasks
@app.get("/api/tasks", response_model=list[TodoSchema])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    sql = select(Todo)
    result = await db.execute(sql)
    if not result:
        raise HTTPException(status_code=404, detail="No tasks found")
    tasks = result.scalars().all()
    return tasks

# Create a new task
@app.post("/api/tasks", response_model=TodoSchema)
async def create_task(todo: TodoCreateSchema, db: AsyncSession = Depends(get_db)):
    new_task = Todo(**todo.dict())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

# Get a task by ID
@app.get("/api/tasks/{task_id}", response_model=TodoSchema)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    sql = select(Todo).where(Todo.id == task_id)
    result = await db.execute(sql)
    task = result.scalar_one_or_none()
    return task

# Update a task by ID
@app.patch("/api/tasks/{task_id}", response_model=TodoSchema)
async def update_task(task_id: int, data: TodoUpdateSchema,  db: AsyncSession = Depends(get_db)):
    task = await db.get(Todo, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    await db.commit()
    await db.refresh(task)
    return task

# Delete a task by ID
@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.get(Todo, task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    await db.delete(result)
    await db.commit()
    return {"message": "Task deleted successfully"}