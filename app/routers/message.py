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

@router.post("/sendMsg/{id_userA}/to/{id_userB}/{sessionName}")
def send_message(id_userA: int, id_userB: int, sessionName: str, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    session = crud.get_session_by_user_ids(id_userA, id_userB, db)
    if not session:
        crud.create_session(db, id_userA, id_userB, sessionName)
    msg = crud.create_message(db, message)

    return msg