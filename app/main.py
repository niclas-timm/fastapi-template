import uvicorn
from fastapi import FastAPI, Depends, Response, status
from db.db import engine
import db.models as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def front():
    return {"Hello:": "My World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
