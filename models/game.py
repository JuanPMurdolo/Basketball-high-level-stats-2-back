from db import db


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.String(32), primary_key=True)
    date = db.Column(db.String(32), nullable=False)
    local_team_id = db.Column(db.String(32), db.ForeignKey("teams.id"), nullable=False)
    visitor_team_id = db.Column(db.String(32), db.ForeignKey("teams.id"), nullable=False)
    local_team = db.relationship("Team", foreign_keys=[local_team_id])
    visitor_team = db.relationship("Team", foreign_keys=[visitor_team_id])
    local_score = db.Column(db.Integer, nullable=False)
    visitor_score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    season = db.Column(db.String(32), nullable=False)
    season_type = db.Column(db.String(32), nullable=False)
    status = db.Column(db.String(32), nullable=False)
    post_season = db.Column(db.Boolean, nullable=False)
    home_team_wins = db.Column(db.Boolean, nullable=False)
    referees = db.Column(db.String(128), nullable=False)
    court = db.Column(db.String(128), nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id"), nullable=False)
    local_players = db.relationship("Player", secondary="game_local_players", lazy="subquery", backref="local_games")
    visitor_players = db.relationship("Player", secondary="game_visitor_players", lazy="subquery", backref="visitor_games")
    # Especifica las claves foráneas en la relación
    local_players_stats = db.relationship("PlayerStats", secondary="game_local_players", lazy="subquery",
                                          primaryjoin="and_(Game.id == GameLocalPlayers.game_id, PlayerStats.id == GameLocalPlayers.stats_id)",
                                          secondaryjoin="and_(GameLocalPlayers.player_id == Player.id, PlayerStats.id == GameLocalPlayers.stats_id)",
                                          backref="local_games")
    
    visitor_players_stats = db.relationship("PlayerStats", secondary="game_visitor_players", lazy="subquery",
                                            primaryjoin="and_(Game.id == GameVisitorPlayers.game_id, PlayerStats.id == GameVisitorPlayers.stats_id)",
                                            secondaryjoin="and_(GameVisitorPlayers.player_id == Player.id, PlayerStats.id == GameVisitorPlayers.stats_id)",
                                            backref="visitor_games")
    
    local_team_stats = db.relationship("TeamStats", secondary="game_local_players", lazy="subquery",
                                       primaryjoin="and_(Game.id == GameLocalPlayers.game_id, TeamStats.id == GameLocalPlayers.stats_id)",
                                       secondaryjoin="and_(GameLocalPlayers.team_id == Team.id, TeamStats.id == GameLocalPlayers.stats_id)",
                                       backref="local_games")
    
    visitor_team_stats = db.relationship("TeamStats", secondary="game_visitor_players", lazy="subquery",
                                         primaryjoin="and_(Game.id == GameVisitorPlayers.game_id, TeamStats.id == GameVisitorPlayers.stats_id)",
                                         secondaryjoin="and_(GameVisitorPlayers.team_id == Team.id, TeamStats.id == GameVisitorPlayers.stats_id)",
                                         backref="visitor_games")