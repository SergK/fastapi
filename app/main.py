from typing import Union
from pydantic import BaseModel, EmailStr, conint
from fastapi import FastAPI, HTTPException

app = FastAPI()


# User data model
class User(BaseModel):
    username: str
    email: EmailStr
    number_of_tasks: conint(ge=0)

# In-memory user database
users_db = {}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users")
def create_user(user: User):
    user_id = len(users_db) + 1
    users_db[user_id] = user.dict()
    return users_db[user_id]

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user.dict()
    return users_db[user_id]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted"}
