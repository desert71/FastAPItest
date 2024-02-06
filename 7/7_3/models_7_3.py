from pydantic import BaseModel

class UserCredentials(BaseModel):
    username: str
    password: str

class UserData(BaseModel):
    user_id: int
    username: str
    email: str