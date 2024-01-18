from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    password: str

class Impr_User(BaseModel):
    username: str
    password: str
    role: Optional[str] = None 