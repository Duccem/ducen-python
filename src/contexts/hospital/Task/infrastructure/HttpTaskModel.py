from pydantic import BaseModel
class TaskModel(BaseModel):
  id: str
  name: str
  description: str
  status: str
