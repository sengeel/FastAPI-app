from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schema.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

def destroy (db : Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(db : Session, request: schema.Blog, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'updated'

def show(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}
    return blog