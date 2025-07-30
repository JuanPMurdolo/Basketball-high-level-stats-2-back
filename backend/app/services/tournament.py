from app.repositories.tournament import TournamentRepository
from sqlalchemy.orm import Session
from app.schemas.tournament import TournamentCreate, TournamentUpdate


class TournamentService:
    def __init__(self, db: Session):
        self.tournament_repository = TournamentRepository(db)

    def create_tournament(self, tournament: TournamentCreate):
        return self.tournament_repository.create_tournament(
            name=tournament.name,
            start_date=tournament.start_date,
            end_date=tournament.end_date
        )

    def get_tournament_by_id(self, tournament_id: int):
        return self.tournament_repository.get_tournament_by_id(tournament_id)

    def get_all_tournaments(self):
        return self.tournament_repository.get_all_tournaments()

    def update_tournament(self, tournament_id: int, tournament: TournamentUpdate):
        return self.tournament_repository.update_tournament(
            tournament_id=tournament_id,
            name=tournament.name,
            start_date=tournament.start_date,
            end_date=tournament.end_date
        )

    def delete_tournament(self, tournament_id: int):
        return self.tournament_repository.delete_tournament(tournament_id)

