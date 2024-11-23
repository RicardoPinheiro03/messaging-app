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
    session_id: int

class MessageCreate(MessageBase):
    pass

class SessionBase(BaseModel):
    name: str

class SessionBaseWithUsers(SessionBase):
    user_a_id: int
    user_b_id: int

class SessionCreate(SessionBase):
    pass