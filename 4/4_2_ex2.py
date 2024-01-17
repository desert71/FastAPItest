from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from models.model_4_1 import User
import jwt

app = FastAPI()
oath2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "my_f_sec_key"
ALORITHM = "HS256"

USERS_DATA = [{"username": "admin", "password": "adminpass"}, 
              {"username": "adminnnn", "password": "adminpass321"}]

# Создание JWT токена на основе нашего ключа, данных и алгоритма
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALORITHM)

# Получение User'а по токену
def get_user_from_token(token: str = Depends(oath2_scheme)):
    try:
        playload = jwt.decode(token, SECRET_KEY, algorithms=[ALORITHM])
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
async def login(user_in: User):
    for user in USERS_DATA:
        if user.get("username") == user_in.username and user.get("password") == user_in.password:
            return {"access_token": create_jwt_token({"sub": user_in.username}), "token_type": "bearer"}
    return {"error": "Invalid credentials"}

# Защищенный путь для информации о пользователе
@app.get('/about_me')
async def about_me(current_user: str = Depends(get_user_from_token)):
    user = get_user(current_user)
    if user:
        return user
    return {"error": "User not aound"}