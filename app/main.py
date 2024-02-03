from fastapi import FastAPI, HTTPException
from models import User

app = FastAPI()

# In-memory 'database'
users_db = {}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()

@app.post("/users")
def create_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[user.username] = user
    return user.to_dict()

@app.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return user.to_dict()

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"detail": "User deleted"}
