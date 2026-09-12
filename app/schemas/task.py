########
# TaskCreate   → lo que entra
# TaskResponse → lo que sale
# TaskModel    → lo que guarda SQLAlchemy
#########

from pydantic import BaseModel

# Clases
class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False
    priority: int = 1

# TaskResponse hereda a TaskCreate, tiene todo lo que tiene TaskCreate, mas id
class TaskResponse(TaskCreate):
    id: int

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    priority: int | None = None
