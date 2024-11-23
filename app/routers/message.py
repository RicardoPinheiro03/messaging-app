from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/createUser/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.post("/sendMsg/{idOfUserA}/to/{idOfUserB}")
def send_message(idOfUserA: int, idOfUserB: int, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    # TODO: Add logic for session creation and message storage.
    pass