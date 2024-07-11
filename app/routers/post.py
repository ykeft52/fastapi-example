from fastapi import FastAPI,Depends,status,HTTPException,Response,APIRouter
from .. import models,schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from .. import oauth2
from sqlalchemy import func

router =APIRouter(
                     tags=['Posts'])
@router.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    
    new_post =models.Post(**post.dict())
       
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
@router.get("/posts",response_model =list[schemas.PostResponse])
def get_posts(db:Session=Depends(get_db),current_user:int =Depends(oauth2.get_current_user)):
    result = models.Post(func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter =True).group_by(models.Post.id)
    return result
    
@router.get("/posts/{id}",response_model =schemas.PostResponse)
def get_post(id:int,db:Session=Depends(get_db),current_user:int =Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Post with id:{id} was not found")
    return post
@router.delete("/posts/{id}",status_code =status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db)):
      post = db.query(models.Post).filter(models.Post.id==id)
      if post.first()==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Post with id:{id} does not exist")
      post.delete(synchronize_session =False)
      db.commit()
      return Response(status_code =status.HTTP_204_NO_CONTENT)
@router.put("/posts/{id}")
def update_post(id:int,updated_post:schemas.PostCreate,db:Session=Depends(get_db)):
      post_query= db.query(models.Post).filter(models.Post.id==id)
      post =post_query.first()
      if post==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Post with id:{id} does not exist")
      post_query.update(title =update_post.title,content =update_post.content,published =update_post.published,synchronize_session=False)
      db.commit()
      
      return post_query.first()
