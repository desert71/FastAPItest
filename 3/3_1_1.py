from fastapi import FastAPI
from models.model_3 import UserCreate

user_app = FastAPI()

@user_app.post("/create_user")
async def create_user(user: UserCreate):
    return user