from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.db import get_db
from app.core.auth import get_current_user, get_current_superuser
from app.models.user import User
from app.schemas.user import UserCreate, UserOut, UserUpdate, UserTeamAssignment
from app.services.user import UserService

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_superuser)
):
    """Create a new user (superuser only)."""
    user_service = UserService(db)
    
    # Check if user already exists
    if user_service.get_user_by_email(user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    if user_service.get_user_by_username(user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    return user_service.create_user(user)

@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    """Get current user information."""
    return current_user

@router.get("/", response_model=List[UserOut])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_superuser)
):
    """Get all users (superuser only)."""
    user_service = UserService(db)
    return user_service.get_users(skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserOut)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_superuser)
):
    """Get user by ID (superuser only)."""
    user_service = UserService(db)
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_superuser)
):
    """Update user (superuser only)."""
    user_service = UserService(db)
    user = user_service.update_user(user_id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/assign-teams")
def assign_teams_to_user(
    assignment: UserTeamAssignment,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_superuser)
):
    """Assign teams to a user (superuser only)."""
    user_service = UserService(db)
    result = user_service.assign_teams_to_user(assignment.user_id, assignment.team_ids)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Teams assigned successfully"}

@router.get("/{user_id}/teams")
def get_user_teams(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_superuser)
):
    """Get teams assigned to a user (superuser only)."""
    user_service = UserService(db)
    teams = user_service.get_user_teams(user_id)
    return {"teams": teams}
