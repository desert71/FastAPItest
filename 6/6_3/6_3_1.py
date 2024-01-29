from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from models import User

app = FastAPI()
Users = {
    1: {
    "username": "Vasya",
    "age": "22",
    "email": "Vasya@email.com",
    "password": "123456789",
    "phone": "phone_number"
    },
    2: {
    "username": "Petya",
    "age": "19",
    "email": "Petya@email.com",
    "password": "999777666",
    "phone": "phone_number2"
    }
}
global i
i=3

@app.post('/create_user')
async def create_user(usr: User):
    global i
    Users[i] = usr
    i+=1
    return {"message": "Пользователь создан", **Users}

@app.get('/user/{user_id}')
async def get_user(user_id: int):
    try:
        return Users[user_id]
    except Exception as ex:
        return {"err": "Нет такого пользователя"}
