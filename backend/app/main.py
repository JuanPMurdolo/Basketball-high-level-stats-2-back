from fastapi import FastAPI
from app.core.db import engine
from app.routes.tournament import router as tournament_router
from app.routes.team import router as team_router
from app.routes.player import router as player_router
from app.routes.match import router as match_router
from app.routes.stats import router as stats_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tournament_router)
app.include_router(team_router)
app.include_router(player_router)
app.include_router(match_router)
app.include_router(stats_router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}