from marshmallow import Schema, fields, validate

class StatsSchema(Schema):
    id = fields.Int(dump_only=True)
    game_id = fields.Int()
    date = fields.Date()
    minutes_played = fields.Int(default=0)
    field_goals = fields.Int(default=0)
    field_goal_attempts = fields.Int(default=0)
    field_goal_percentage = fields.Float(default=0)
    three_pointers = fields.Int(default=0)
    three_point_attempts = fields.Int(default=0)
    three_point_percentage = fields.Float(default=0)
    two_pointers = fields.Int(default=0)
    two_point_attempts = fields.Int(default=0)
    two_point_percentage = fields.Float(default=0)
    effective_field_goal_percentage = fields.Float(default=0)
    free_throws = fields.Int(default=0)
    free_throw_attempts = fields.Int(default=0)
    free_throw_percentage = fields.Float(default=0)
    offensive_rebounds = fields.Int(default=0)
    defensive_rebounds = fields.Int(default=0)
    total_rebounds = fields.Int(default=0)
    assists = fields.Int(default=0)
    steals = fields.Int(default=0)
    blocks = fields.Int(default=0)
    turnovers = fields.Int(default=0)
    personal_fouls = fields.Int(default=0)
    points = fields.Int(default=0)

class PlayerByGameStatsSchema(StatsSchema):
    player_id = fields.Int()
    player_efficiency_rating = fields.Float(default=0)

class TeamHistoryTrackerSchema(Schema):
    team_id = fields.Int()
    actual_team = fields.Bool()
    seasons = fields.List(fields.Str())
    beggining_of_contract = fields.Date()
    end_of_contract = fields.Date()

class PlayerSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    #One player can only be in one team but played in a longer amount during his carreer and that needs to be tracked  
    historical_team_id = fields.Nested(TeamHistoryTrackerSchema)
    picture = fields.Str()
    position = fields.Str()
    date_of_birth = fields.Date()
    games = fields.Int(default=0)
    games_started = fields.Int(default=0)
    stats = fields.Nested(StatsSchema)
    #This will be the sum of all the stats
    all_stats = fields.Nested(StatsSchema)

class TeamSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    abbreviation = fields.Str()
    city = fields.Str()
    conference = fields.Str()
    division = fields.Str()
    court = fields.Str()
    alternative_court = fields.Str(default="")
    players = fields.List(fields.Nested(PlayerSchema), default=[])

class GameSchema(Schema):
    id = fields.Str(dump_only=True)
    local_team_id = fields.Int()
    local_team_name = fields.Str()
    visitor_team_id = fields.Int()
    visitor_team_name = fields.Str()
    local_score = fields.Int()
    visitor_score = fields.Int()
    date = fields.Date()
    season = fields.Str()
    status = fields.Str()
    postseason = fields.Bool()
    referees = fields.List(fields.Str())
    court = fields.Str()
    local_players = fields.List(fields.Nested(PlayerSchema), max_items=12)
    local_players_stats = fields.Nested(PlayerByGameStatsSchema, max_items=12)
    visitor_players = fields.List(fields.Nested(PlayerSchema), max_items=12)
    visitor_players_stats = fields.Nested(PlayerByGameStatsSchema, max_items=12)
    local_team_stats = fields.Nested(StatsSchema, max_items=1)
    visitor_team_stats = fields.Nested(StatsSchema, max_items=1)

class ControlValuesSchema(Schema):
    stats_control_values = fields.Dict()

class TournamentSchema(Schema):
    id = fields.Str(dump_only=True)
    games = fields.List(fields.Nested(GameSchema))
    season = fields.Str()
    season_type = fields.Str()

class StatsSchema(Schema):
    data = fields.Str()