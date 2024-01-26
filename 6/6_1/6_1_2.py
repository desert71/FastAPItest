from typing import Any, Dict, Optional
from typing_extensions import Annotated, Doc
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from models import ErrorResponse

app = FastAPI()

# Класс исключений A
class CustomExceptionA(HTTPException):
    def __init__(self):
        err = ErrorResponse(error_code = 406, error_mgs = "Запретный этаж")
        super().__init__(status_code=err.error_code, detail=err.error_mgs)

# Класс исключений B
class CustomExceptionB(HTTPException):
    def __init__(self):
        err = ErrorResponse(error_code = 402, error_mgs="Ты не заплатил!!! Плоти")
        super().__init__(status_code=err.error_code, detail=err.error_mgs)

# Обработчик ошибок (error handler) для класса CustomExceptionA
@app.exception_handler(CustomExceptionA)
async def custom_exception_handler(request: Request, exc: CustomExceptionA):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

# Обработчик ошибок (error handler) для класса CustomExceptionB
@app.exception_handler(CustomExceptionB)
async def custom_exception_handler(request: Request, exc: CustomExceptionB):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

@app.get('/floors/{floor_num}')
async def get_item(floor_num: int):
    if floor_num == 13:
        raise CustomExceptionA
    else:
        return {"msg": f"Вы выбрали {floor_num} этаж"}
    
@app.get('/room_servise/{payment}/')
async def get_servises(payment: bool):
    if payment:
        return {"msg": "Выбирайте услугу"}
    else:
        raise CustomExceptionB