from datetime import date
class Task:
  def __init__(self, id: str, name: str, description: str, status: str, created_at: date, updated_at: date):
    self.id = id
    self.name = name
    self.description = description
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at

  @classmethod
  def from_primitives(cls, data):
    return cls(data['id'], data['name'], data['description'], data['status'], date.fromisoformat(data['created_at']), date.fromisoformat(data['updated_at']))

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
