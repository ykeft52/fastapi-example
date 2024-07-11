from fastapi import FastAPI,Depends,status,HTTPException,APIRouter
from .. import models,schemas,utils
from .. database import engine,get_db
from sqlalchemy.orm import Session
router= APIRouter(tags=['Users'])
@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
     check_user =db.query(models.User).filter(models.User.email ==user.email).first()
     if check_user :
          raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
                              detail=f"user with email:{user.email} already registered")
     hashed_password =utils.hash(user.password)
     user.password = hashed_password
     new_user = models.User(**user.dict())
     db.add(new_user)
     db.commit()
     db.refresh(new_user)
     return new_user
@router.get("/users/{id}",response_model =schemas.UserResponse)
def get_user(id:int,db:Session =Depends(get_db)):
     my_user = db.query(models.User).filter(models.User.id==id).first()
     if my_user ==None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id:{id} does not exist")
     return my_user