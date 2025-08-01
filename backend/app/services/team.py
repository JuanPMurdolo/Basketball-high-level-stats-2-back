from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.team import Team
from app.schemas.team import TeamCreate, TeamUpdate

class TeamService:
    def __init__(self, db: Session):
        self.db = db

    def get_team_by_id(self, team_id: int) -> Optional[Team]:
        """Get team by ID."""
        return self.db.query(Team).filter(Team.id == team_id).first()

    def get_all_teams(self, skip: int = 0, limit: int = 100) -> List[Team]:
        """Get all teams with pagination."""
        return self.db.query(Team).offset(skip).limit(limit).all()

    def get_teams_by_ids(self, team_ids: List[int], skip: int = 0, limit: int = 100) -> List[Team]:
        """Get teams by list of IDs."""
        return self.db.query(Team).filter(Team.id.in_(team_ids)).offset(skip).limit(limit).all()

    def create_team(self, team: TeamCreate) -> Team:
        """Create a new team."""
        db_team = Team(**team.dict())
        self.db.add(db_team)
        self.db.commit()
        self.db.refresh(db_team)
        return db_team

    def update_team(self, team_id: int, team_update: TeamUpdate) -> Optional[Team]:
        """Update team."""
        team = self.get_team_by_id(team_id)
        if not team:
            return None

        update_data = team_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(team, field, value)

        self.db.commit()
        self.db.refresh(team)
        return team

    def delete_team(self, team_id: int) -> bool:
        """Delete team."""
        team = self.get_team_by_id(team_id)
        if not team:
            return False

        self.db.delete(team)
        self.db.commit()
        return True
