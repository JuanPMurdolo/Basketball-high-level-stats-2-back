from sqlalchemy.orm import Session
from app.models import Team
from app.schemas import TeamCreate


class TeamRepository:
    def __init__(self, db):
        self.db = db

    def get_team_by_id(self, team_id: int):
        return self.db.query(Team).filter(Team.id == team_id).first()

    def get_all_teams(self):
        return self.db.query(Team).all()

    def create_team(self, team: TeamCreate):
        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)
        return team

    def update_team(self, team_id: int, updated_team: Team):
        team = self.get_team_by_id(team_id)
        if team:
            for key, value in updated_team.__dict__.items():
                setattr(team, key, value)
            self.db.commit()
            self.db.refresh(team)
            return team
        return None

    def delete_team(self, team_id: int):
        team = self.get_team_by_id(team_id)
        if team:
            self.db.delete(team)
            self.db.commit()
            return True
        return False