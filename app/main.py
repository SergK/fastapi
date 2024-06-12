from typing import Union

from fastapi import FastAPI
from .config import Settings

app = FastAPI()
settings = Settings()


@app.get("/")
def read_root():
    return {"Hello": "World"}


from typing import Union
from fastapi import FastAPI

app = FastAPI()

users_db = {}

@app.post("/users/")
def create_user(user_id: int, name: str):
    if user_id in users_db:
        return {"error": "User already exists."}
    users_db[user_id] = {"name": name}
    return users_db[user_id]

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return users_db.get(user_id, {"error": "User not found."})

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str):
    if user_id not in users_db:
        return {"error": "User not found."}
    users_db[user_id] = {"name": name}
    return users_db[user_id]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        return {"error": "User not found."}
    del users_db[user_id]
    return {"message": "User deleted."}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/config")
def get_oidc_config():
    return {
        "issuer": settings.OIDC_ISSUER,
        "client_id": settings.OIDC_CLIENT_ID,
        "client_secret": settings.OIDC_CLIENT_SECRET
    }