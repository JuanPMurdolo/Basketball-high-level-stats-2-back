from db import db

class PlayerByGameStats(db.Model):
    __tablename__ = "player_by_game_stats"
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)
    minutes_played = db.Column(db.Integer, nullable=True)
    field_goals = db.Column(db.Integer, nullable=True)
    field_goal_attempts = db.Column(db.Integer, nullable=True)
    free_throw_percentage = db.Column(
        db.Float,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: (context.current_parameters['free_throws'] + 1) /
                                 (context.current_parameters['free_throw_attempts'] + 1) - 1
    )
    three_pointers = db.Column(db.Integer, nullable=True)
    three_point_attempts = db.Column(db.Integer, nullable=True)
    three_point_percentage = db.Column(
        db.Float,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: (context.current_parameters['three_pointers'] + 1) /
                                 (context.current_parameters['three_point_attempts'] + 1) - 1
    )
    two_pointers = db.Column(db.Integer, nullable=True)
    two_point_attempts = db.Column(db.Integer, nullable=True)
    two_point_percentage = db.Column(
        db.Float,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: (context.current_parameters['two_pointers'] + 1) /
                                 (context.current_parameters['two_point_attempts'] + 1) - 1
    )
    free_throws = db.Column(db.Integer, nullable=True)
    free_throw_attempts = db.Column(db.Integer, nullable=True)
    free_throw_percentage = db.Column(
        db.Float,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: (context.current_parameters['free_throws'] + 1) /
                                 (context.current_parameters['free_throw_attempts'] + 1) - 1
    )
    offensive_rebounds = db.Column(db.Integer, nullable=True)
    defensive_rebounds = db.Column(db.Integer, nullable=True)
    total_rebounds = db.Column(
        db.Integer,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: context.current_parameters['offensive_rebounds'] +
                                 context.current_parameters['defensive_rebounds']
    )
    assists = db.Column(db.Integer, nullable=True)
    steals = db.Column(db.Integer, nullable=True)
    blocks = db.Column(db.Integer, nullable=True)
    turnovers = db.Column(db.Integer, nullable=True)
    personal_fouls = db.Column(db.Integer, nullable=True)
    points = db.Column(
        db.Integer,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: (context.current_parameters['field_goals'] * 2) +
                                 (context.current_parameters['three_pointers'] * 3) +
                                 context.current_parameters['free_throws']
    )
    offensive_rebound_percentage = db.Column(
        db.Float,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: (context.current_parameters['offensive_rebounds'] + 1) /
                                 (context.current_parameters['total_rebounds'] + 1) - 1
    )
    
    defensive_rebound_percentage = db.Column(
        db.Float,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: (context.current_parameters['defensive_rebounds'] + 1) /
                                 (context.current_parameters['total_rebounds'] + 1) - 1
    )