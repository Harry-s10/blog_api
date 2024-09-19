from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas
from .user_crud import get_user_id


def get_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Requested {blog_id} not found.")
    return blog


def get_all_blogs(db: Session):
    return db.query(models.Blog).all()


def create_blog(db: Session, request: schemas.BlogCreate, current_user: schemas.User):
    new_blog = models.Blog(**request.model_dump(), owner_id=get_user_id(current_user.email, db))
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update_blog(db: Session, blog_id: int, request: schemas.BlogCreate):
    blog = get_blog(db, blog_id)
    blog.update(request.model_dump())
    db.commit()
    return "Updated"


def remove_blog(db: Session, blog_id: int):
    blog = get_blog(db, blog_id)
    blog.delete(synchronize_session=False)
    db.commit()
    return "Deleted"
