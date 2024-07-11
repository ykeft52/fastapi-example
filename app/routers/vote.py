from fastapi import FastAPI,Depends,status,HTTPException,APIRouter
from .. import models,schemas,oauth2,database

from sqlalchemy.orm import Session

router =APIRouter(
                     tags=['votes'])
@router.posts("/votes",status_code =status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:Session =Depends(database.get_db),current_user:int =Depends(oauth2.get_current_user)):
     vote_query= db.query(models.Vote).filter(models.Vote.post_id ==vote.post_id,models.Vote.user_id==current_user.id)
     found_vote = vote_query.first()
     if(vote.dir ==1):
        if found_vote :
               raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail =f"user {current_user.id} has already voted with {vote.post_id}")
     new_vote =models.Vote(post_id = vote.post_id,user_id = current_user.id)
     db.add(new_vote)
     db.commit()
     return {"MESSAGE":"SUCCESSFULLY VOTED"}
    
    

    
          
