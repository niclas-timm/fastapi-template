from fastapi import Depends, FastAPI
from app.db.db import engine
from app.db import models
from app.api.routers import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get('/')
async def front():
    return "Lieber Arthur, du bist ein kleiner Pisser :)!"
