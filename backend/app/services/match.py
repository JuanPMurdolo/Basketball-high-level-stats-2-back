from app.repositories.match import MatchRepository


class MatchService:
    def __init__(self, db: Session):
        self.match_repository = MatchRepository(db)

    def create_match(self, match: MatchCreate):
        return self.match_repository.create_match(match)

    def get_matches_by_zone(self, zona_id: int):
        return self.match_repository.get_matches_by_zone(zona_id)

    def get_all_matches(self):
        return self.match_repository.get_all_matches()