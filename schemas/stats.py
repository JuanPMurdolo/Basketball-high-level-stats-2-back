from marshmallow import Schema, fields

class StatsSchema(Schema):
    id = fields.Int(dump_only=True)
    public_id = fields.Str(required=True)

    fieldGoalsMade = fields.Int(required=True)
    fieldGoalsAttempted = fields.Int(required=True)
    threePointersMade = fields.Int(required=True)
    threePointersAttempted = fields.Int(required=True)
    twoPointersMade = fields.Int(required=True)
    twoPointersAttempted = fields.Int(required=True)
    freeThrowsMade = fields.Int(required=True)
    freeThrowsAttempted = fields.Int(required=True)
    offensiveRebounds = fields.Int(required=True)
    defensiveRebounds = fields.Int(required=True)
    assists = fields.Int(required=True)
    steals = fields.Int(required=True)
    blocks = fields.Int(required=True)
    turnovers = fields.Int(required=True)
    personalFouls = fields.Int(required=True)
    points = fields.Int(required=True)
    Poss = fields.Float(required=True)
    Plays = fields.Float(required=True)
    PPP = fields.Float(required=True)
    PPT1 = fields.Float(required=True)
    PPT2 = fields.Float(required=True)
    PPT3 = fields.Float(required=True)
    PPPT1 = fields.Float(required=True)
    PPPT2 = fields.Float(required=True)
    PPPT3 = fields.Float(required=True)
    fieldGoalPercentage = fields.Float(required=True)
    threePointPercentage = fields.Float(required=True)
    twoPointPercentage = fields.Float(required=True)
    freeThrowPercentage = fields.Float(required=True)
    player_public_id = fields.Str(required=True)
    game_public_id = fields.Str(required=True)
    team_public_id = fields.Str(required=True)