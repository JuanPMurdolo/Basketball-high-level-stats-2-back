from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import tournament

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tournament.router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
