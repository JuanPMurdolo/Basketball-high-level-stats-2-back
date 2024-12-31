from marshmallow import Schema, fields, validate

class PlainTeamSchema(Schema):
    id = fields.Integer(required=True, validate=validate.Range(min=0))
    name = fields.String(required=False, validate=validate.Length(min=1))
    city = fields.String(required=False, validate=validate.Length(min=1))

class PlainPlayerSchema(Schema):
    id = fields.Integer(required=True, validate=validate.Range(min=0))
    name = fields.String(required=True, validate=validate.Length(min=1))
    age = fields.Integer(required=False, validate=validate.Range(min=0, max=100))
    first_division = fields.Boolean(required=False)
    position = fields.String(required=False, validate=validate.Length(min=1))
    years_active = fields.Integer(required=False, validate=validate.Range(min=0))
    teams = fields.String(required=False, validate=validate.Length(min=1))

class PlainStatSchema(Schema):
    id = fields.Integer(required=False, validate=validate.Range(min=0))
    points = fields.Integer(required=False, validate=validate.Range(min=0))
    rebounds_def = fields.Integer(required=False, validate=validate.Range(min=0))
    rebounds_off = fields.Integer(required=False, validate=validate.Range(min=0))
    rebounds_total = fields.Integer(required=False, validate=validate.Range(min=0))
    assists = fields.Integer(required=False, validate=validate.Range(min=0))
    steals = fields.Integer(required=False, validate=validate.Range(min=0))
    blocks = fields.Integer(required=False, validate=validate.Range(min=0))
    field_goal_attempts = fields.Integer(required=False, validate=validate.Range(min=0))
    field_goal_makes = fields.Integer(required=False, validate=validate.Range(min=0))
    free_throw_attempts = fields.Integer(required=False, validate=validate.Range(min=0))
    free_throw_makes = fields.Integer(required=False, validate=validate.Range(min=0))
    three_point_attempts = fields.Integer(required=False, validate=validate.Range(min=0))
    three_point_makes = fields.Integer(required=False, validate=validate.Range(min=0))
    year = fields.Integer(required=False, validate=validate.Range(min=0))
    player_id = fields.Integer(required=False, validate=validate.Range(min=0))

class PlainTournamentSchema(Schema):
    id = fields.Integer(required=True, validate=validate.Range(min=0))
    name = fields.String(required=False, validate=validate.Length(min=1))
    year = fields.Integer(required=False, validate=validate.Range(min=0))

class TeamSchema(PlainTeamSchema):
    players = fields.Nested(PlainPlayerSchema, many=True)
    tournament = fields.Nested(PlainTournamentSchema)

class TournamentSchema(PlainTournamentSchema):
    teams = fields.Nested(PlainTeamSchema, many=True)


class PlayerSchema(PlainPlayerSchema):
    team = fields.Nested(PlainTeamSchema)
    stats = fields.Nested(PlainStatSchema, many=True)

