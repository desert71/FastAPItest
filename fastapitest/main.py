from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.model_1 import User

app = FastAPI()
user = User(id = 1, name = "John Doe", age= 25)

def is_adult(age: int) -> bool:
    return age > 18

@app.get("/")
async def root():
    return FileResponse("index.html", status_code=200)

@app.get("/custom")
async def custom_root():
    return {"message": "This is custom page :)"}

@app.get("/users")
async def get_user():
    return user

@app.post("/user")
async def post_user(user: User):
    return {**dict(user), "is_adult": is_adult(user.age)} 