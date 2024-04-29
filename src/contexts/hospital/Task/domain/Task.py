from datetime import date
class Task:
  def __init__(self, id: str, name: str, description: str, status: str, created_at: date, updated_at: date):
    self.id = id
    self.name = name
    self.description = description
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at

  @staticmethod
  def from_primitives(data: dict[str, str]):
    return Task(data.id, data.name, data.description, data.status, data.created_at, data.updated_at)

  def create(id: str, name: str, description: str, status: str):
    return Task(id, name, description, status, date.today(), date.today())

  def to_primitives(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'status': self.status,
      'created_at': self.created_at.isoformat(),
      'updated_at': self.updated_at.isoformat()
    }
