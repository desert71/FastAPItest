from pydantic import BaseModel, conint, EmailStr, constr
from typing import Union, Optional

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    age: conint(gt=18)
    email: EmailStr
    password: constr(min_length=8, max_length=16)
    phone: Optional[str] = "Unknown"

class ErrorResponse(BaseModel):
    error_code: int
    error_mgs: str
    error_detail: str = None