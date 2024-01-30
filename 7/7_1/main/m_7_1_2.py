from fastapi import FastAPI, HTTPException, Request
from fastapi.routing import APIRoute, APIRouter
from fastapi.responses import JSONResponse
from models import User, ErrorResponse
from datetime import datetime

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

app = FastAPI()


#________________________Обработка_исключений________________________________________________________________________________________________

class UserNotFoundException(HTTPException):
    def __init__(self) -> None:
        err = ErrorResponse(error_code=404, error_mgs="Пользователь не найден", error_detail="Вы ввели не верный id пользователя :(")
        super().__init__(status_code = err.error_code, detail = err.error_detail, headers={"X-ErrorHandleTime": str(datetime.now(tz=3))})

@app.exception_handler(UserNotFoundException)
async def UserNotFoundException_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
        headers= exc.headers
    )


#__________________________Методы_API___________________________________________________________________________________________________________

async def create_user(usr: User):
    global i
    Users[i] = usr
    i+=1
    return {"message": "Пользователь создан", **Users}

async def get_user(user_id: int):
    try:
        return Users[user_id]
    except Exception as ex:
        raise UserNotFoundException

async def del_user(user_id: int):
    try:
        del Users[user_id]
        return {"message": "Пользователь удален", **Users}
    except Exception as ex:
        raise UserNotFoundException


#_________________________Пути_API_____________________________________________________________________________________________________________

routes = [
    APIRoute(path="/create_user", endpoint=create_user, methods=["POST"]),
    APIRoute(path="/get_user/{user_id}", endpoint=create_user, methods=["GET"]),
    APIRoute(path="/del_user/{user_id}", endpoint=create_user, methods=["DELETE"])
]

app.include_router(APIRouter(routes=routes))