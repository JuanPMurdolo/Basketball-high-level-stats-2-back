from sqlalchemy.orm import Session
from app.models import Player
from app.schemas import PlayerCreate

class PlayerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_player(self, player: PlayerCreate):
        db_player = Player(**player.dict())
        self.db.add(db_player)
        self.db.commit()
        self.db.refresh(db_player)
        return db_player

    def get_players_by_team(self, equipo_id: int):
        return self.db.query(Player).filter(Player.equipo_id == equipo_id).all()

    def get_all_players(self):
        return self.db.query(Player).all()