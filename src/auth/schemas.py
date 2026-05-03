from pydantic import BaseModel, Field
from datetime import datetime as dt
import uuid


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: dt
    updated_at: dt


class UserCreateModel(BaseModel):
    username: str = Field(max_length=12)
    email: str = Field(max_length=40)
    password: str = Field(min_length=8)
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)


class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=8)
