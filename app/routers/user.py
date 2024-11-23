from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/createUser/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/getUser/{id}", response_model=schemas.UserBase)
def get_user_route(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, userID=id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

@router.post("/user/{id}/profilePictureUpload/{mediaFile}")
def upload_profile_picture(id: int, mediaFile: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, id=id)
    if not user:
        return {"error": "User not found"}
    user.profile_picture = mediaFile
    db.commit()
    db.refresh(user)
    return {"message": f"Profile picture updated for user {id}"}