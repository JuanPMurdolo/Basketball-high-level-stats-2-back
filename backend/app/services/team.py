from app.repostories.team import TeamRepository
from sqlalchemy.orm import Session
from app.schemas import TeamCreate

class TeamService:
    def __init__(self, db: Session):
        self.team_repository = TeamRepository(db)

    def get_team_by_id(self, team_id: int):
        return self.team_repository.get_team_by_id(team_id)

    def get_all_teams(self):
        return self.team_repository.get_all_teams()

    def create_team(self, team: TeamCreate):
        return self.team_repository.create_team(team)

    def update_team(self, team_id: int, updated_team: Team):
        return self.team_repository.update_team(team_id, updated_team)

    def delete_team(self, team_id: int):
        return self.team_repository.delete_team(team_id)