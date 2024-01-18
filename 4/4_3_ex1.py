from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from typing import Optional, Annotated
from models.model_4_1 import Impr_User

app = FastAPI()

SECRET_KEY = "my_second_secret_key"
ALORITHM = "HS256"

USERS_DATA = {"admin": {"username": "admin", "password": "adminpass", 
                        "role": "admin"}, 
              "user": {"username": "user", "password": "userpass", 
                       "role": "user"}}

# Для авторизации по токену
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Создание JWT токена на основе нашего ключа, данных и алгоритма
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALORITHM)

# Получение юзера по токену  
def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        playload = jwt.decode(token, SECRET_KEY, algorithms=[ALORITHM])
        return playload.get("sub")
    except jwt.ExpiredSignatureError:
        # Истечения срока действия токена
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        # Ошибка декодирования токена
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Получение данных пользователя из "Базы данных"    
def get_user(username: str):
    if username in USERS_DATA:
        user_data = USERS_DATA[username]
        return Impr_User(**user_data)
    return None

# Путь получения токена
@app.post('/token/')
async def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_from_db = get_user(user_data.username)
    if user_from_db is None or user_from_db.password != user_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentialssss",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": create_jwt_token({"sub": user_data.username})}

# Защищенный путь для администраторов
@app.get('/admin/')
async def get_for_admin(cur_user: str = Depends(get_user_from_token)):
    user_data = get_user(cur_user)
    if user_data.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "not authorized",
        )
    return {"message": "Welcome Admin!"}

# Защищенный путь для обычных пользователей
@app.get('/user/')
async def get_for_user(cur_user: str = Depends(get_user_from_token)):
    user_data = get_user(cur_user)
    if user_data.role != "user":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "not authorized",
        )
    return {"message": "Hello User!"}