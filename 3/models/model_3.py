from pydantic import BaseModel

class UserCreate (BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool

class product (BaseModel):
    product_id: int
    name: str
    category: str
    price: float

class auth_user(BaseModel):
    username: str
    password: str