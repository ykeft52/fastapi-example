from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from . import schemas,database,models
from sqlalchemy.orm import Session
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7 "
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def create_access_token(data: dict):
    #add the payload which is the data
    to_encode =data.copy()
     # get the current time and add 30minutes to it 
    expire =datetime.now() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    # add the expiring time using the update function
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token:str,credentials_exception):  
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithm =ALGORITHM)
        id:str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data  = schemas.TokenData(id =id)
    except JWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token:str = Depends(oauth2_scheme),db:Session =Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token,credentials_exception)
    user = db.query(models.User).filter(models.User.id ==token.id).first()
    return user