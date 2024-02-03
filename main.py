rom fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel, EmailStr, conint

# Define the User model with validations

class User(BaseModel):
    username: str
    email: EmailStr
    number_of_tasks: conint(ge=0)  # Greater than or equal to 0

# In-memory database to store users
users_db = {}

@app.get('/users/{user_id}')
def get_user(user_id: int):
    # Retrieve a specific user by their ID
    return users_db.get(user_id)

@app.post('/users')
def create_user(user: User):
    # Create a new user
    user_id = max(users_db.keys(), default=0) + 1
    users_db[user_id] = user.dict()
    return users_db[user_id]

@app.put('/users/{user_id}')
def update_user(user_id: int, user: User):
    # Update an existing user by their ID
    if user_id in users_db:
        users_db[user_id].update(user.dict())
        return users_db[user_id]
    else:
        raise HTTPException(status_code=404, detail='User not found')

@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    # Delete a user by their ID
    if user_id in users_db:
        del users_db[user_id]
        return {'message': 'User deleted successfully'}
    else:
        raise HTTPException(status_code=404, detail='User not found')
