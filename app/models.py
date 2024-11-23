from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    profile_picture = Column(String, nullable=True)
    location = Column(String, nullable=True)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    text = Column(String, nullable=False)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_a_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_b_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Unique constraint to ensure no duplicate sessions between the same users
    __table_args__ = (UniqueConstraint('user_a_id', 'user_b_id', name='_user_a_b_uc'),)

    # Relationships (optional, for easier access)
    user_a = relationship("User", foreign_keys=[user_a_id])
    user_b = relationship("User", foreign_keys=[user_b_id])