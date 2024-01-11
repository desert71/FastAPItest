from fastapi import FastAPI
from models.model_1 import Feedback

app = FastAPI()

fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

feedback = []

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id in fake_users.keys():
        return fake_users[user_id]
    return {"error": "User not found"}


@app.post("/feedback")
async def post_feedback(fb: Feedback):
    feedback.append(fb)
    return {"message": f"Feedback received. Thank you, {fb.name}"}


@app.get("/feedbacks")
async def get_feedback():
    return feedback