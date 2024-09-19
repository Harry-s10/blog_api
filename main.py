import uvicorn
from fastapi import FastAPI

from .app_db import database
from .app_db import models
from .routers import blog, login, user

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)

if __name__ == '__main__':
    uvicorn.run(app, reload=True)
