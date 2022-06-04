import uvicorn
from fastapi import FastAPI, Depends, Response, status
from app.db.db import engine
import app.db.models as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def front():
    return "Hallo Arthur, du bist ein kleiner Pisser."
