from fastapi import APIRouter
from src.contexts.hospital.Task.application.CreateTask import TaskCreator
from src.contexts.hospital.Task.infrastructure.MongoTaskRepository import MongoTaskRepository
from src.contexts.hospital.Task.infrastructure.HttpTaskModel import TaskModel
from ..connections.database import database

task_router = APIRouter()

@task_router.get("/tasks")
async def get_tasks():
  return {"data": "Task data"}

@task_router.get("/tasks/{task_id}")
async def get_task(task_id: str):
  return {"data": task_id}

@task_router.put("/tasks")
async def update_task(task: TaskModel):
  print(task)
  creator = TaskCreator(MongoTaskRepository(database=database))
  await creator.run(task)
  return {"message": "success"}

@task_router.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
  return {"data": task_id}
