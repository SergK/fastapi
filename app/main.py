from typing import Union

from fastapi import FastAPI
from .config import Settings

app = FastAPI()
settings = Settings()


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