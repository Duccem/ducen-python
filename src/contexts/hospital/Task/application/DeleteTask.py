from src.contexts.hospital.Task.domain.Task import Task
from src.contexts.hospital.Task.domain.TaskRepository import TaskRepository
class TaskDeleter:
  def __init__(self, repository: TaskRepository):
    self.repository = repository

  async def run(self, id: str):
    await self.repository.delete_task(id)
