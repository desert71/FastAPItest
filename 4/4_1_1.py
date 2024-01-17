from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.model_4_1 import User

app = FastAPI()
security = HTTPBasic()

USER_DATA = [User(**{"username": "user1", "password": "pass1"}), 
             User(**{"username": "user2", "password": "pass2"})]

def authentification(credential: HTTPBasicCredentials = Depends(security)):
    user = get_user(credential.username)
    if user is None or user.password != credential.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentional", headers={"WWW-Authenticate": "Basic"})
    return user

def get_user(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None


@app.get('/login')
async def get_auth(user: User = Depends(authentification)):
    return {"message": "You got my secret, welcome"}