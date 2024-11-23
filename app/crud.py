from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, userID: int):
    db_user = db.get(models.User, userID)
    return db_user

def create_message(db: Session, text: str, session_id: int):
    db_message = models.Message(text=text, session_id=session_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def create_session(db: Session, idUserA: int, idUserB: int, name: str):
    db_user_A = db.get(models.User, idUserA)
    db_user_B = db.get(models.User, idUserB)

    db_session = models.Session(user_a_id=idUserA, user_b_id=idUserB, name=name)
    db.add(db_session)
    db.commit() 
    db.refresh(db_session)
    return db_session

def get_session_by_user_ids(db: Session, id_userA: int, id_userB: int):
    db_session = db.query(models.Session).filter(
        models.Session.user_a_id == id_userA,
        models.Session.user_b_id == id_userB
    ).first()
    return db_session

def get_session(db: Session, session_id: int):
    db_session = db.get(models.Session, session_id)
    return db_session
