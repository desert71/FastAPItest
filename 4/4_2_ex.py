import jwt

SECRET_KEY = "my_f_sec_key"
ALORITHM = "HS256"

USERS_DATA = [{"username": "admin", "password": "adminpass"}, {"username": "adminnnn", "password": "adminpass321"}]

# Создание JWT токена на основе нашего ключа, данных и алгоритма
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALORITHM)

# Получение User'а по токену
def get_user_from_token(token: str):
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

## Пример

# Кодирование токена 
token = create_jwt_token({"sub": "adminnnn"})
print(token)

#Декодирование токена
username = get_user_from_token(token)
print(username)

# Проверка username в базе данных
current_user = get_user(username)
print(current_user)
