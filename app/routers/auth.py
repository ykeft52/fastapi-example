from fastapi import APIRouter,HTTPException,Response,status,Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from .. import database, models,schemas,utils,oauth2
router =APIRouter(tags=['Authentication'])

@router.post("/login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user =db.query(models.User).filter(models.User.email==user_credentials.username).first()

    if not user:
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,
          detail = f"user with email:{user_credentials.email} does not exist")
  
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    access_token = oauth2.create_access_token(data ={"user_id":user.id})

    return {"access_token" : access_token,"token_type" :"bearer"}