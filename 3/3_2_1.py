from fastapi import FastAPI, Cookie, Response, Request
from models.model_3 import auth_user
import random
import string

auth_app = FastAPI()

fake_db = [{"username": "vasya", "password": "pass123", "session_token": "token1"}, {"username": "katya", "password": "pass321", "session_token": "token2"}]

@auth_app.post('/login')
async def login(user_auth: auth_user, response: Response):
    for i in fake_db:
        if (i["username"] == user_auth.username) and (i["password"] == user_auth.password):

            i["session_token"] = ''.join(random.sample(string.ascii_letters + string.digits, 5))
            response.set_cookie(key="session_token", value=i["session_token"], httponly=True)
            return {"message": "Авторизация прошла успешно"}
    return {"message":"Ты кто, чёрт?"}


@auth_app.get('/user')
async def get_user(request: Request):
    session_token = request.cookies.get("session_token")
    if session_token:
        for i in fake_db:
            if i["session_token"] == session_token:
                return i
        return {"Токен неправильный"}  
    else:
        return {"Нет токена"}
    
