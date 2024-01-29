from typing import Any
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from models import User

app = FastAPI()

class Create_user_exception(HTTPException):
    def __init__(self, status_code: int, detail: Any = None) -> None:
        super().__init__(status_code= 418, detail= "Необходимые условия для создания пользователя не выполнены :(")

@app.exception_handler(RequestValidationError)
async def create_user_exception_handler(req: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code= 418,
        content={"error": "Необходимые условия для создания пользователя не выполнены :("}
    )


@app.post('/create_user')
async def create_user(usr: User = None) -> dict:
    if usr:
        return usr.dict()
    else:
        raise Create_user_exception
    # try:
    #     return usr.dict()
    # except Exception as ex:
    #     raise Create_user_exception

