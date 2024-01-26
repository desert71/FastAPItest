from typing import Any, Dict, Optional
from typing_extensions import Annotated, Doc
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# класс пользовательской обработки ошибок
class CustomException(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)


# Обработчик ошибок (error handler) для класса CustomException
@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


# Обработчик глобальных исключений, который перехватывает все необработанные исключения
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


# маршрут, который вызывает пользовательское исключение
@app.get('/items/{item_id}/')
async def read_item(item_id: int):
    if item_id == 42:
        raise CustomException(detail="Item not found", status_code=404)
    result = 1/0
    return {"item_id": item_id} 