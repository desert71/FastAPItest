from typing import Any, Dict, Optional
from typing_extensions import Annotated, Doc
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from models import User, ErrorResponse
from datetime import datetime

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

class UserNotFoundException(HTTPException):
    def __init__(self) -> None:
        err = ErrorResponse(error_code=404, error_mgs="Пользователь не найден", error_detail="Вы ввели не верный id пользователя :(")
        super().__init__(status_code = err.error_code, detail = err.error_detail, headers={"X-ErrorHandleTime": str(datetime.now(tz=3))})

class InvalidUserDataException(RequestValidationError):
    def __init__(self) -> None:
        err = ErrorResponse(error_code=418, error_mgs="Не правильные данные", error_detail="Для создания пользователя введите корректные данные :)")
        super().__init__(status_code = err.error_code, detail = err.error_detail)

@app.exception_handler(UserNotFoundException)
async def UserNotFoundException_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
        headers= exc.headers
    )

@app.exception_handler(RequestValidationError)
async def UserNotFoundException_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=418,
        content={"error": "Для создания пользователя введите корректные данные :)"}
    )

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
        raise UserNotFoundException
