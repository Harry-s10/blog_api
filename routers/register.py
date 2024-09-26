from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app_db.database import get_db
from app_db.schemas import UserCreate, UserDisplay
from app_db.user_crud import create

router = APIRouter(
        prefix="/register",
        tags=["Login"]
)


@router.post("/", response_model=UserDisplay)
def register_user(request: UserCreate, db: Session = Depends(get_db)):
    return create(request, db)
