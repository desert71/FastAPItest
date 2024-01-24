from fastapi import FastAPI, HTTPException, status
from databases import Database
from models import UserCreate, UserReturn

app = FastAPI()

DATABASE_URL = "postgresql://Alex:Alex_password@localhost/myDataBase"

database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup_database():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_database():
    await database.disconnect()

@app.post('/users/', response_model=UserReturn)
async def create_user(user: UserCreate):
    query = "INSERT INTO users (username, email) VALUES (:username, :email) RETURNING id"
    values = {"username": user.username, "email": user.email}
    try:
        user_id = await database.execute(query=query, values=values)
        return{**user.dict(), "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Не получилось создать пользователя :(")