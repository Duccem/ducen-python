from abc import ABC, abstractmethod
from src.contexts.hospital.Task.domain.Task import Task

class TaskRepository(ABC):
  @abstractmethod
  async def getTask(self, task_id: str) -> Task:
    pass
  @abstractmethod
  async def search(self) -> list[Task]:
    pass
  @abstractmethod
  async def save(self, task: Task) -> None:
    pass
  @abstractmethod
  async def delete_task(self, task_id: str) -> None:
    pass
