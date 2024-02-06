from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.routing import APIRouter, APIRoute
from models_7_3 import UserCredentials, UserData

app = FastAPI()

# Псевдо БД
fake_users_db = [
    {
        "user_id": 1,
        "username": "user123",
        "password": "secretpassword",
        "email": "user@example.com"
    }
]

# Псевдо хранилище сессий
sessions = {}

# @app.get('/items/{item_id}')
# def read_item(item_id: int):
#     return{"item_id": item_id}

# Проверяем наличие пользователя и возвращаем куки
def login(user_creds: UserCredentials, response: Response):
    for user in fake_users_db:
        if user["username"] == user_creds.username and user["password"] == user_creds.password:
            response.set_cookie(key="session_cookie", value="my_random_cookie")
            sessions[user_creds.username] = "my_random_cookie"
            return {"message": "Login seccessful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Возвращаем данные по кукам, если они достоверны 
def protected_data(request: Request):
    for username, cookie in sessions.items():
        if request.cookies.get("session_cookie") and cookie == request.cookies.get("session_cookie"):
            user = get_user_by_username(username)
            return UserData(**user)
    raise HTTPException(status_code=401, detail="Bad cookie")

# Вспомогательная функция по извлечению пользователя из псевдо-БД
def get_user_by_username(username: str):
    for user in fake_users_db:
        if user.get("username") == username:
            return user
    else:
        raise HTTPException(status_code=401, detail="User not found")

routes = [
    APIRoute(path='/login/', endpoint=login, methods=["POST"]),
    APIRoute(path='/protected_data/', endpoint=protected_data, methods=["GET"], response_model=UserData),

]

app.include_router(APIRouter(routes=routes))