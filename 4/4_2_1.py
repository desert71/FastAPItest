from fastapi import FastAPI, Depends, Request
#from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse, Response
from models.model_4_1 import User
from datetime import datetime, timedelta
import jwt

app = FastAPI()
#oath2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "my_f_sec_key"
ALORITHM = "HS256"

USERS_DATA = [{"username": "admin", "password": "adminpass"}, 
              {"username": "adminnnn", "password": "adminpass321"}]

# Создание JWT токена на основе нашего ключа, данных и алгоритма
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALORITHM)

# Получение User'а по токену
#def get_user_from_token(res: Response '''token: str = Depends(oath2_scheme)'''):
def get_user_from_token(req: Request):
    try:
        playload = jwt.decode(req.headers["Autharization"], SECRET_KEY, algorithms=[ALORITHM])
        return playload.get("sub")
    except jwt.ExpiredSignatureError:
        # Истечения срока действия токена
        pass
    except jwt.InvalidTokenError:
        # Ошибка декодирования токена
        pass


def get_user(username: str):
    for user in USERS_DATA:
        if user.get("username") == username:
            return user
    return None

# Пуль для аутентификации, но так лучше не делать
@app.post('/login')
async def login(res: Response, user_in: User):
    for user in USERS_DATA:
        if user.get("username") == user_in.username and user.get("password") == user_in.password:
            res.headers["Autharization"] = create_jwt_token({"sub": user_in.username, "exp": datetime.utcnow() + timedelta(seconds=60*7)})
            return {"message": "Вы успешно авторизированы"} #RedirectResponse("/protected_source" ''', {"message": "Вы успешно авторизированы"}''')
            #{"access_token": create_jwt_token({"sub": user_in.username, "exp": datetime.utcnow + timedelta(seconds=60*7)}), "token_type": "bearer"}
    return {"error": "Invalid credentials"}

# Защищенный путь для информации о пользователе
@app.get('/protected_source')
async def get_protected_source(req: Request, current_user: str = Depends(get_user_from_token)):
    user = get_user(current_user)
    if user:
        return user, req.headers["autharization"]
    return {"error": "User not found"}