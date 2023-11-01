from enum import Enum
from typing import Literal, NewType, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    ## Config Class needed for pydantic since it can only validate JSON. These 2 lines below make sure it will be JSON
    class Config:
        from_attributes = True 


class PostResponse(BaseModel):
    Post: Post
    likes: int

    class Config:
        from_attributes = True 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class VoteDirection(Enum):
    DOWN = 0
    UP = 1

class Vote(BaseModel):
    post_id: int
    dir: VoteDirection