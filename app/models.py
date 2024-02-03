from pydantic import BaseModel, Field, validator
import re

class User(BaseModel):
    username: str
    email: str
    number_of_tasks: int = Field(ge=0)

    @validator('email')
    def validate_email(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('Invalid email format')
        return v
