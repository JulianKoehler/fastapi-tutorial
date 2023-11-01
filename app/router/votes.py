from fastapi import Response, Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, db, models, oauth2

router = APIRouter(prefix="/vote", tags=["Post voting"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, 
         db: Session = Depends(db.get_db), 
         current_user: models.User | None = Depends(oauth2.get_current_user)):

    post_exists = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post_exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id '{vote.post_id}' does not exist")
    
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    vote_on_post_exists = vote_query.first()
    
    if vote.dir == schemas.VoteDirection.UP:
        if vote_on_post_exists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.id} has already liked this post")
        
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()

        return { "message": "Succesfully voted on post"}
    
    if vote.dir == schemas.VoteDirection.DOWN:
        if not vote_on_post_exists:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()

        return { "message": "The Like was successfully removed" }
