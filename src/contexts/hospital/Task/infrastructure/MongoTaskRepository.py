from ..domain.TaskRepository import TaskRepository
from ..domain.Task import Task
from motor.motor_asyncio import AsyncIOMotorDatabase
class MongoTaskRepository(TaskRepository):
  def __init__(self, database: AsyncIOMotorDatabase):
    self.database = database

  async def getTask(self, task_id: str) -> Task:
    task = await self.database.tasks.find_one({'_id': task_id})
    print(task)
    return Task.from_primitives(task) if task else None

  async def search(self) -> list[Task]:
    tasks: list[Task] = []
    async for task in self.database.tasks.find():
      tasks.append(Task.from_primitives(task))
    return tasks

  async def save(self, task: Task) -> None:
    await self.database.tasks.update_one({ 'id': task.id }, { '$set': task.to_primitives() }, upsert=True)

  async def delete_task(self, task_id: str) -> None:
    await self.database.tasks.delete_one({ 'id': task_id })
