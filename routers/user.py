from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app_db import database, schemas, user_crud
from authentication import get_current_active_user

router = APIRouter(
        prefix="/user",
        tags=['Users']
)


@router.post("/", response_model=schemas.UserDisplay)
def create_user(request: schemas.UserCreate, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(get_current_active_user)):
    """Create new user"""
    return user_crud.create(request, db)


@router.get("/{id}", response_model=schemas.UserDisplay)
def get_user(id: int, db: Session = Depends(database.get_db)):
    """Get user detail based on ID"""
    return user_crud.get_user(id, db)


@router.get("/{id}/blogs", response_model=schemas.UserBlogs)
def get_user_blogs(id: int, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(get_current_active_user)):
    """Get all user's blogs based on ID"""
    return user_crud.get_user(id, db)
