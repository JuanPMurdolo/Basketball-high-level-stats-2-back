from app.repositories.stats import StatsRepository

class StatsService:
    def __init__(self, db: Session):
        self.stats_repository = StatsRepository(db)

    def create_stats(self, stats: StatsCreate):
        return self.stats_repository.create_stats(stats)

    def get_stats_by_match(self, match_id: int):
        return self.stats_repository.get_stats_by_match(match_id)

    def get_stats_by_player(self, player_id: int):
        return self.stats_repository.get_stats_by_player(player_id)

    def get_all_stats(self):
        return self.stats_repository.get_all_stats()