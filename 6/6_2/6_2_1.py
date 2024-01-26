from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models import Item

app = FastAPI()



@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(status_code=400, content={"error": str(exc)})

@app.post('/items')
async def create_item(item: Item):
    try:
        if item.price < 0:
            raise ValueError("Какая отрицательная стоимость, ты о чём")
        return {"message": "Предмет создан успешно", "item": item}
    except ValueError as ve:
        raise ve
    