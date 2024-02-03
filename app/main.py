from fastapi import FastAPI, HTTPException
from models import User
from typing import List

app = FastAPI()

users_db = []

@app.post("/users")
def create_user(user: User):
    users_db.append(user.dict())
    return user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = next((u for u in users_db if u['username'] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    idx = next((i for i, u in enumerate(users_db) if u['username'] == user_id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[idx] = user.dict()
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    idx = next((i for i, u in enumerate(users_db) if u['username'] == user_id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    users_db.pop(idx)
    return {"detail": "User deleted"}
