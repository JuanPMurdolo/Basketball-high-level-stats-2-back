from app.repostories.player import PlayerRepository

class PlayerService:
    def __init__(self, db: Session):
        self.player_repository = PlayerRepository(db)

    def create_player(self, player: PlayerCreate):
        return self.player_repository.create_player(player)

    def get_players_by_team(self, equipo_id: int):
        return self.player_repository.get_players_by_team(equipo_id)

    def get_all_players(self):
        return self.player_repository.get_all_players()