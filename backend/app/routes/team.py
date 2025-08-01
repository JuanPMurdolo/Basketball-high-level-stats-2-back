from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.db import get_db
from app.core.auth import get_current_user, get_user_teams, check_team_access
from app.models.user import User
from app.schemas.team import TeamCreate, TeamOut, TeamUpdate
from app.services.team import TeamService

router = APIRouter()

@router.post("/", response_model=TeamOut)
def create_team(
    team: TeamCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new team."""
    team_service = TeamService(db)
    return team_service.create_team(team)

@router.get("/", response_model=List[TeamOut])
def get_teams(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get teams accessible to the current user."""
    team_service = TeamService(db)
    user_team_ids = get_user_teams(current_user, db)
    
    if not user_team_ids:  # Superuser or no restrictions
        return team_service.get_all_teams(skip=skip, limit=limit)
    else:
        return team_service.get_teams_by_ids(user_team_ids, skip=skip, limit=limit)

@router.get("/{team_id}", response_model=TeamOut)
def get_team(
    team_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get team by ID."""
    if not check_team_access(current_user, team_id, db):
        raise HTTPException(status_code=403, detail="Access denied to this team")
    
    team_service = TeamService(db)
    team = team_service.get_team_by_id(team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.put("/{team_id}", response_model=TeamOut)
def update_team(
    team_id: int,
    team_update: TeamUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update team."""
    if not check_team_access(current_user, team_id, db):
        raise HTTPException(status_code=403, detail="Access denied to this team")
    
    team_service = TeamService(db)
    team = team_service.update_team(team_id, team_update)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.delete("/{team_id}")
def delete_team(
    team_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete team."""
    if not check_team_access(current_user, team_id, db):
        raise HTTPException(status_code=403, detail="Access denied to this team")
    
    team_service = TeamService(db)
    if not team_service.delete_team(team_id):
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team deleted successfully"}
