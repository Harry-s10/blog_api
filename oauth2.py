from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from fastapi import Depends, status, HTTPException
from .app_db import schemas
from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(auth_token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Couldn't validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
    )
    return token.verify_token(auth_token, credentials_exception)


def add_user_id_request(request: schemas.Blog, current_user: str = Depends(get_current_user)):
    request.model_fields_set.add("user_id", )
