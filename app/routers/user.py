from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/createUser/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/getUser/{id}")
def get_user(user: schemas.UserBase, db: Session = Depends(get_db), id: int):
    user = 

@router.post("/user/{id}/profilePictureUpload/{mediaFile}")
def upload_profile_picture(id: int, mediaFile: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, id=id)  # You would need to add `get_user` in `crud.py`.
    if not user:
        return {"error": "User not found"}
    user.profile_picture = mediaFile
    db.commit()
    db.refresh(user)
    return {"message": f"Profile picture updated for user {id}"}