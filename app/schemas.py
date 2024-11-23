from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    profile_picture: Optional[str] = None
    location: Optional[str] = None

class UserCreate(UserBase):
    pass

class MessageBase(BaseModel):
    text: str

class MessageCreate(MessageBase):
    pass