import uvicorn
from fastapi import FastAPI

from app_db import models
from app_db.database import engine
from routers import blog, login, register, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)
app.include_router(register.router)

if __name__ == '__main__':
    uvicorn.run(app, reload=True)
