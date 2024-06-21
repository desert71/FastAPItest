import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def my_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["Text_info"] = "Hellow from middleware )))"
    return response

@app.get("/")
def index():
    print("Привет из основного обработчика пути")
    return {"message": "Hello, world!"}
