from datetime import datetime
from typing import List

from pydantic import BaseModel, SecretStr


class BlogBase(BaseModel):
    title: str
    body: str


class BlogCreate(BlogBase):
    timestamp: datetime


class Blog(BlogBase):
    id: int
    owner_id: int
    model_config: dict = {
        "from_attributes": True
    }


class UserBase(BaseModel):
    name: str
    email: str
    model_config = {
        "from_attributes": True
    }


class UserCreate(UserBase):
    password: str


class User(UserCreate):
    id: int
    is_active: bool
    model_config: dict = {
        "from_attributes": True
    }


class UserDisplay(UserBase):
    id: int
    is_active: bool


class UserBlogs(UserBase):
    blogs: List[BlogCreate] = []


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class BlogDisplay(BlogBase):
    id: int
    creator: UserBase
    timestamp: datetime
    model_config = {
        "from_attributes": True
    }
