from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.core.security import verify_token
from app.models.user import User
from app.models.user_team import UserTeam
from typing import List

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Get the current authenticated user."""
    token = credentials.credentials
    payload = verify_token(token)
    
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Get the current active user."""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_current_superuser(current_user: User = Depends(get_current_user)) -> User:
    """Get the current superuser."""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return current_user

def get_user_teams(user: User, db: Session) -> List[int]:
    """Get list of team IDs that the user has access to."""
    if user.is_superuser:
        # Superusers have access to all teams
        return []  # Empty list means access to all
    
    user_teams = db.query(UserTeam).filter(UserTeam.user_id == user.id).all()
    return [ut.team_id for ut in user_teams]

def check_team_access(user: User, team_id: int, db: Session) -> bool:
    """Check if user has access to a specific team."""
    if user.is_superuser:
        return True
    
    user_team = db.query(UserTeam).filter(
        UserTeam.user_id == user.id,
        UserTeam.team_id == team_id
    ).first()
    
    return user_team is not None
