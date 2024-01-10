from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.model_1 import User

app = FastAPI()
user = User(id = 1, name = "John Doe")

@app.get("/")
async def root():
    return FileResponse("index.html", status_code=200)

@app.get("/custom")
async def custom_root():
    return {"message": "This is custom page :)"}

@app.get("/users")
async def get_user(user: User):
    return {"id": user.id, "name": user.name}