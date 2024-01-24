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

# Create
@app.post('/users/', response_model=UserReturn)
async def create_user(user: UserCreate):
    query = "INSERT INTO users (username, email) VALUES (:username, :email) RETURNING id"
    values = {"username": user.username, "email": user.email}
    try:
        user_id = await database.execute(query=query, values=values)
        return{**user.dict(), "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Не получилось создать пользователя :(")

# Read    
@app.get('/user/{user_id}', response_model=UserReturn)
async def get_user(user_id: int):
    query = "SELECT * FROM users WHERE id = :user_id"
    values = {"user_id": user_id}
    try:
        result = await database.fetch_one(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Не получилось взять данные пользователя из базы данных")
    if result:
        return UserReturn(username=result["username"], email=result["email"])
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Что-то пользователя не нашлось :(")
    
# Update
@app.put('/user/{user_id}', response_model=UserReturn)
async def update_user(user_id: int, user: UserCreate):
    query = "UPDATE users SET username = :username, email = :email WHERE id = :user_id"
    values = {"user_id": user_id, "username": user.username, "email": user.email}
    try:
        await database.execute(query=query, values=values)
        return {**user.dict(), "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Не удалось обновить пользователя, сори  :(")