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

class TeamSchema(PlainTeamSchema):
    id = fields.Integer(required=True)

class PlayerSchema(PlainPlayerSchema):
    id = fields.Integer(required=True)

class CoachSchema(PlainCoachSchema):
    id = fields.Integer(required=True)