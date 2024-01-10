from fastapi import FastAPI

calc_app = FastAPI()

@calc_app.post("/calculate")
def calculate(num1: int, num2: int):
    return {"result": num1 + num2}
