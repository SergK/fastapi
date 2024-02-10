from fastapi import FastAPI, HTTPException
from models import User

app = FastAPI()

# In-memory 'database'
users_db = {}

@app.get("/users/{user_id}")
"""
Get a user from the in-memory database by user_id.

:param user_id: The ID of the user to retrieve.
:return: The user's data as a dictionary.
:raises HTTPException: If the user is not found.
"""
def get_user(user_id: str):
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()

@app.post("/users")
"""
Create a new user in the in-memory database.

:param user: The user data to create.
:return: The created user's data as a dictionary.
:raises HTTPException: If the username already exists.
"""
def create_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[user.username] = user
    return user.to_dict()

@app.put("/users/{user_id}")
"""
Update a user in the in-memory database by user_id.

:param user_id: The ID of the user to update.
:param user: The new user data to update.
:return: The updated user's data as a dictionary.
:raises HTTPException: If the user is not found.
"""
def update_user(user_id: str, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return user.to_dict()

@app.delete("/users/{user_id}")
"""
Delete a user from the in-memory database by user_id.

:param user_id: The ID of the user to delete.
:return: A message indicating the user was deleted.
:raises HTTPException: If the user is not found.
"""
def delete_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"detail": "User deleted"}
