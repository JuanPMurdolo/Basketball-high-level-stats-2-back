from marshmallow import Schema, fields, validate

class PlainTeamSchema(Schema):
    name = fields.String(required=False, validate=validate.Length(min=1))
    city = fields.String(required=False, validate=validate.Length(min=1))

class PlainPlayerSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    age = fields.Integer(required=False, validate=validate.Range(min=0, max=100))
    first_division = fields.Boolean(required=False)
    position = fields.String(required=False, validate=validate.Length(min=1))
    years_active = fields.Integer(required=False, validate=validate.Range(min=0))
    teams = fields.String(required=False)

class PlainCoachSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    age = fields.Integer(required=False, validate=validate.Range(min=0, max=100))
    teams = fields.String(required=False)

class PlainStatsSchema(Schema):
    points = fields.Integer(required=True, validate=validate.Range(min=0))
    defensive_rebounds = fields.Integer(required=True, validate=validate.Range(min=0))
    offensive_rebounds = fields.Integer(required=True, validate=validate.Range(min=0))
    rebounds = fields.Integer(required=True, validate=validate.Range(min=0))
    assists = fields.Integer(required=True, validate=validate.Range(min=0))
    steals = fields.Integer(required=True, validate=validate.Range(min=0))
    blocks = fields.Integer(required=True, validate=validate.Range(min=0))
    turnovers = fields.Integer(required=True, validate=validate.Range(min=0))
    fouls = fields.Integer(required=True, validate=validate.Range(min=0))
    minutes = fields.Integer(required=True, validate=validate.Range(min=0))
    field_goals_made = fields.Integer(required=True, validate=validate.Range(min=0))
    field_goals_attempted = fields.Integer(required=True, validate=validate.Range(min=0))
    two_points_made = fields.Integer(required=True, validate=validate.Range(min=0))
    two_points_attempted = fields.Integer(required=True, validate=validate.Range(min=0))
    three_points_made = fields.Integer(required=True, validate=validate.Range(min=0))
    three_points_attempted = fields.Integer(required=True, validate=validate.Range(min=0))
    free_throws_made = fields.Integer(required=True, validate=validate.Range(min=0))
    free_throws_attempted = fields.Integer(required=True, validate=validate.Range(min=0))


class TeamSchema(PlainTeamSchema):
    id = fields.Integer(required=True)

class PlayerSchema(PlainPlayerSchema):
    id = fields.Integer(required=True)

class CoachSchema(PlainCoachSchema):
    id = fields.Integer(required=True)

class StatsSchema(PlainStatsSchema):
    id = fields.Integer(required=True)