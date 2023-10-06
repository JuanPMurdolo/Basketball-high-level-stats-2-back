from marshmallow import Schema, fields, validate

class PlainPlayerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    position = fields.Str(required=True, validate=validate.Length(min=1))

class PlainStatsSchema(Schema):
    id = fields.Int(dump_only=True)
    player_id = fields.Nested(PlainPlayerSchema, dump_only=True)
    field_goal_attempts = fields.Int(required=True)
    field_goal_made = fields.Int(required=True)
    field_goal_percentage = fields.Float()

class PlayerSchema(PlainPlayerSchema):
    stats = fields.Nested(PlainStatsSchema, many=True)

class PlayerStatsSchema(Schema):
    id = fields.Int(dump_only=True)
    player_id = fields.Nested(PlainPlayerSchema, dump_only=True)
    stats_id = fields.Nested(PlainStatsSchema, dump_only=True)
