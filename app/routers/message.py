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

@router.post("/sendMsg/{user_send_id}/to/{user_receive_id}/{session_name}")
def send_message(user_send_id: int, user_receive_id: int, session_name: str, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    session = crud.get_session_by_user_ids(user_send_id, user_receive_id, db)
    print(session.session_id)
    if not session:
        crud.create_session(db, user_send_id, user_receive_id, session_name)
    
    msg = crud.create_message(db, message, session_id)

    return msg