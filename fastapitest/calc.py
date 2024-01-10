from fastapi import FastAPI

calc_app = FastAPI()

@calc_app.post("/calc")
async def calc(num1: int = 5, num2: int = 10):
    return {"result": num1+num2}
