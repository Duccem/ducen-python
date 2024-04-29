from ..domain.TaskRepository import TaskRepository
from ..domain.Task import Task
class TaskCreator:
  def __init__(self, repository: TaskRepository):
    self.repository = repository

  async def run(self, data: dict[str, str]) -> None:
    task = Task.create(data.id, data.name, data.description, data.status)
    await self.repository.save(task)
