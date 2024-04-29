from ..domain.Task import Task
from ..domain.TaskRepository import TaskRepository
class TaskSearcher:
  def __init__(self, repository: TaskRepository):
    self.repository = repository

  async def run(self) -> list[Task]:
    return await self.repository.search()
