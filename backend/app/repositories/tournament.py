from datetime import datetime
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.core.db import Base
from app.models.tournament import Tournament

class TournamentRepository():
    def __init__(self, db_session):
        self.db_session = db_session

    def create_tournament(self, name: str, start_date: datetime, end_date: datetime):
        new_tournament = Tournament(name=name, start_date=start_date, end_date=end_date)
        self.db_session.add(new_tournament)
        self.db_session.commit()
        return new_tournament

    def get_tournament_by_id(self, tournament_id: int):
        return self.db_session.query(Tournament).filter(Tournament.id == tournament_id).first()

    def get_all_tournaments(self):
        return self.db_session.query(Tournament).all()

    def update_tournament(self, tournament_id: int, name: str = None, start_date: datetime = None, end_date: datetime = None):
        tournament = self.get_tournament_by_id(tournament_id)
        if not tournament:
            return None
        if name:
            tournament.name = name
        if start_date:
            tournament.start_date = start_date
        if end_date:
            tournament.end_date = end_date
        self.db_session.commit()
        return tournament

    def delete_tournament(self, tournament_id: int):
        tournament = self.get_tournament_by_id(tournament_id)
        if not tournament:
            return None
        self.db_session.delete(tournament)
        self.db_session.commit()
        return tournament