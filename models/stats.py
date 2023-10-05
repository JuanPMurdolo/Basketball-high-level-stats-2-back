from db import db

class Stats(db.Model):
    __tablename__ = "stats"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teams = db.relationship('Team', secondary="team_stats", back_populates='stats')
    players = db.relationship('Player', secondary="player_stats", back_populates='stats')
    games_local = db.relationship('Game', secondary="games_stats", back_populates='local_team_stats', overlaps="games_visitor,visitor_team_stats")
    games_visitor = db.relationship('Game', secondary="games_stats", back_populates='visitor_team_stats', overlaps="games_local,local_team_stats")
    games_played = db.Column(db.Integer)
    field_goals = db.Column(db.Integer, nullable=True)
    field_goal_attempts = db.Column(db.Integer, nullable=True)
    field_goal_percentage = db.Column(
        db.Float,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: (context.current_parameters['field_goals'] + 1) /
                                 (context.current_parameters['field_goal_attempts'] + 1) - 1
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
    #to calculate this PTS + REB + AST + STL + BLK − Missed FG − Missed FT - TO) / GP
    player_efficiency_rating = db.Column(
        db.Float,
        nullable=True,
        default=0,
        server_default="0",
        onupdate=lambda context: (((context.current_parameters['points'] +
                                 context.current_parameters['total_rebounds'] +
                                 context.current_parameters['assists'] +
                                 context.current_parameters['steals'] +
                                 context.current_parameters['blocks'] -
                                 (context.current_parameters['field_goal_attempts'] -
                                 context.current_parameters['field_goals']) -
                                 (context.current_parameters['free_throw_attempts'] -
                                 context.current_parameters['free_throws']) -
                                 context.current_parameters['turnovers']))+1 / context.current_parameters['games_played']+1)-1
    )