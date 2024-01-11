from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

class Feedback(BaseModel):
    name: str
    message: str