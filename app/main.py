import uvicorn
from fastapi import FastAPI, Depends, Response, status
from app.db.db import engine
import app.db.models as models
from app.api.routers import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get('/')
def front():
    return "Lieber Arthur, du bist ein kleiner Pisser :)!"
