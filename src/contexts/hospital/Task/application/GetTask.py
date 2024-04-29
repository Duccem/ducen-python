from ..domain.Task import Task
from ..domain.TaskRepository import TaskRepository
class TaskGetter:
  def __init__(self, repository: TaskRepository):
    self.repository = repository

  async def run(self, task_id: str) -> Task:
    task = await self.repository.getTask(task_id)
    return task
