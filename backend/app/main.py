from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.db import engine
from app.models import Base
from app.routes.tournament import router as tournament_router
from app.routes.team import router as team_router
from app.routes.player import router as player_router
from app.routes.match import router as match_router
from app.routes.stats import router as stats_router
from app.routes.spreadsheet import router as spreadsheet_router
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router
from fastapi.responses import RedirectResponse



# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Basketball Stats API",
    description="API for managing basketball tournaments, teams, players, and statistics",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["authentication"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(tournament_router, prefix="/tournaments", tags=["tournaments"])
app.include_router(team_router, prefix="/teams", tags=["teams"])
app.include_router(player_router, prefix="/players", tags=["players"])
app.include_router(match_router, prefix="/matches", tags=["matches"])
app.include_router(stats_router, prefix="/stats", tags=["stats"])
app.include_router(spreadsheet_router, prefix="/spreadsheet", tags=["spreadsheet"])

@app.get("/")
def root():
    """Root endpoint that redirects to API documentation."""
    return RedirectResponse(url="/docs")
    
@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Basketball Stats API is running"}
