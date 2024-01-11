from fastapi import FastAPI

app = FastAPI()

fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id in fake_users.keys():
        return fake_users[user_id]
    return {"error": "User not found"}