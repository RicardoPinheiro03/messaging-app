from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/getSession/{id}", response_model=schemas.SessionBase)
def get_session(id: int, db: Session = Depends(get_db)):
    db_session = crud.get_session(db, session_id=id)
    if not db_session:
        raise HTTPException(status_code=404, detail="Session does not exist")
    
    return db_session

@router.get("/getSessionUsers/{id_userA}/{id_userB}", response_model=schemas.SessionBaseWithUsers)
def get_session_by_user_ids(id_userA: int, id_userB: int, db: Session = Depends(get_db)):
    db_session = crud.get_session_by_user_ids(db, id_userA, id_userB)

    if not session:
        raise HTTPException(status_code=404, detail="Session does not exist")
    
    return db_session