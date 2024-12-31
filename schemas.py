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
    teams = fields.String(required=False)

class PlainCoachSchema(Schema):
    id = fields.Integer(required=True, validate=validate.Range(min=0))
    name = fields.String(required=True, validate=validate.Length(min=1))
    age = fields.Integer(required=False, validate=validate.Range(min=0, max=100))
    teams = fields.String(required=False)
