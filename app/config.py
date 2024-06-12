from pydantic import BaseSettings

class Settings(BaseSettings):
    client_id: str
    client_secret: str
    authorization_endpoint: str
    token_endpoint: str
    userinfo_endpoint: str
    redirect_uri: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'