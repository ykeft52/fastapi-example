from pydantic import BaseModel,EmailStr, conint
from typing import Optional
from datetime import datetime
from pydantic.types import conint
class PostBase(BaseModel):

    title: str
    content:str
    published:bool= True

class PostCreate(PostBase):
    pass
   
class PostResponse(BaseModel):
     title:str
     content:str
     published:bool
     created_at:datetime
     owner_id :int
     class Config:  

        orm_mode = True
class UserCreate(BaseModel):
     email:EmailStr
     password:str
class UserResponse(BaseModel):
     id:int
     email:EmailStr
     created_at:datetime
     owner_id:int
     class Config:
         orm_mode =True
class UserLogin(BaseModel):
    email:EmailStr
    password:str
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Optional[str] =None
class Vote(BaseModel):
    post_id :int
    dir: conint(le =1)