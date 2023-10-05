import json
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import GameSchema, StatsSchema
from .funciones import *
from db import db
from models.game import Game as GameModel
from models.team import Team as TeamModel
from models.player import Player as PlayerModel
from models.stats import Stats as StatsModel

blp = Blueprint(
    "stats", __name__, url_prefix="/stats", description="Operations on stats"
)

@blp.route("")
class Stats(MethodView):
    @blp.response(200, StatsSchema(many=True))
    def get(self):
        return StatsModel.query.all()
    
@blp.route("/<int:id>/player/<int:player_id>")
class StatsPlayer(MethodView):
    @blp.response(200, StatsSchema)
    def get(self, id, player_id):
        stats = StatsModel.query.get_or_404(id)
        player = PlayerModel.query.get_or_404(player_id)
        if player not in stats.players:
            abort(404, message="Player not found in stats")
        player.stats.append(stats)
        db.session.add(stats)
        db.session.add(player)
        db.session.commit()
        return stats
