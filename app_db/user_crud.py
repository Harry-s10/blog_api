from fastapi import HTTPException, status
from pydantic import SecretStr
from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def encrypt(password: SecretStr):
        return pwd_content.hash(str(password))

    @staticmethod
    def verify(plain_password: str, hashed_password: str):
        return pwd_content.verify(plain_password, hashed_password)


def get_user(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user found with ID {user_id}")
    return user


def create(request: schemas.UserCreate, db: Session):
    request.password = Hash.encrypt(request.password)
    new_user = models.User(**request.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
