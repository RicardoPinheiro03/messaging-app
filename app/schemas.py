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

class SessionBase(BaseModel):
    name: str
    pass

class SessionBaseWithUsers(SessionBase):
    id_user_a: int
    id_user_b: int

class SessionCreate(SessionBase):
    pass