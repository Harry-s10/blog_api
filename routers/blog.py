from fastapi import APIRouter, Depends, status
from ..app_db import database, blog_crud, schemas
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from typing import List

from .. import oauth2

router = APIRouter(
        prefix="/blogs",
        tags=['Blogs']
)


@router.get("/{id}", response_model=schemas.BlogDisplay)
def get_blog(id: int, db: Session = Depends(database.get_db)):
    """Get the blog based on the ID"""
    return blog_crud.get_blog(db, id).first()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogBase, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    """Create new blog"""
    new_blog = schemas.BlogCreate(**request.model_dump(), timestamp=datetime.now(timezone.utc))
    return blog_crud.create_blog(db, new_blog, current_user)


@router.get("/", response_model=List[schemas.BlogDisplay])
def get_all_blogs(db: Session = Depends(database.get_db)):
    """Get all the blogs"""
    return blog_crud.get_all_blogs(db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.BlogBase, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    """Update the blog"""
    updated_blog: schemas.BlogCreate = schemas.BlogCreate(**request.model_dump(), timestamp=datetime.now(timezone.utc))
    return blog_crud.update_blog(db, id, updated_blog)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_blog(id: int, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    """Remove the blog"""
    return blog_crud.remove_blog(db, id)
