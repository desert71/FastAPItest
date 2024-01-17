from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.model_4_1 import User

app = FastAPI()
security = HTTPBasic()

USER_DATA = [User(**{"username": "user1", "password": "pass1"}), 
             User(**{"username": "user2", "password": "pass2"})]

def authentificate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user

def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None

@app.get('/protected_resource/')
async def get_protected_resource(user: User = Depends(authentificate_user)):
    return {"message": "You have access to thr protected resource!", "user_info": user}