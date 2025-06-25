from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import tournament, team, player, match, stats

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tournament.router)
app.include_router(team.router)
app.include_router(player.router)
app.include_router(match.router)
app.include_router(stats.router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
