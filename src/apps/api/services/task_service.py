from src.apps.api.connections.database import collection
from src.contexts.hospital.Task.domain.Task import Task

async def get_one_task(task_id: str) -> Task:
  task = await collection.find_one({'_id': task_id})
  return Task(**task)

async def get_tasks() -> list[Task]:
  tasks: list[Task] = []
  async for task in collection.find():
    tasks.append(Task(**task))
  return tasks

async def create_task(task: Task) -> None:
  await collection.insert_one(task.to_primitives())

async def update_task(task: Task) -> None:
  await collection.update_one({'_id': task_id}, {'$set': task}, {'upsert': True})

async def delete_task(task_id: str) -> None:
  await collection.delete_one({ '_id': task_id })
