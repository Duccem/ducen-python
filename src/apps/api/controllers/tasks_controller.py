from fastapi import APIRouter
from src.contexts.hospital.Task.application.CreateTask import TaskCreator
from src.contexts.hospital.Task.application.GetTask import TaskGetter
from src.contexts.hospital.Task.application.SearchTask import TaskSearcher
from src.contexts.hospital.Task.application.DeleteTask import TaskDeleter
from src.contexts.hospital.Task.infrastructure.MongoTaskRepository import MongoTaskRepository
from src.contexts.hospital.Task.infrastructure.HttpTaskModel import TaskModel
from ..connections.database import database

task_router = APIRouter()

@task_router.get("/tasks")
async def get_tasks():
  searcher = TaskSearcher(MongoTaskRepository(database=database))
  tasks = await searcher.run()
  return [task.to_primitives() for task in tasks]

@task_router.get("/tasks/{task_id}")
async def get_task(task_id: str):
  getter = TaskGetter(MongoTaskRepository(database=database))
  task = await getter.run(task_id)
  return task.to_primitives()

@task_router.put("/tasks")
async def update_task(task: TaskModel):
  creator = TaskCreator(MongoTaskRepository(database=database))
  await creator.run(task)
  return {"message": "success"}

@task_router.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
  deleter = TaskDeleter(MongoTaskRepository(database=database))
  await deleter.run(task_id)
  return {"message": "success"}
