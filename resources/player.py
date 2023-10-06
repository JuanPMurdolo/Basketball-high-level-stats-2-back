from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from models import PlayerModel, StatsModel
from db import db
from schemas import PlainStatsSchema, PlayerSchema

playersBlp = Blueprint(
    "players", "players", url_prefix="/players", description="Operations on players"
)

@playersBlp.route("/")
class Player(MethodView):
    @playersBlp.response(200, PlayerSchema(many=True))
    def get(self):
        """List players"""
        return PlayerModel.query.all()
    
    @playersBlp.arguments(PlayerSchema)
    @playersBlp.response(200, PlayerSchema)
    def post(self, player_data):
        """Create a new player"""
        player = PlayerModel(**player_data)
        db.session.add(player)
        db.session.commit()
        return player
    
@playersBlp.route("/<int:player_id>")
class PlayerStats(MethodView):
    @playersBlp.response(200, PlayerSchema)
    def get(self, player_id):
        """Get a player"""
        player = PlayerModel.query.get_or_404(player_id)
        return player
    
    @playersBlp.response(200, PlayerSchema)
    def post(self, player_id):
        player = PlayerModel.query.get_or_404(player_id)
        stats_data = request.json  # Obtener los datos de las estadísticas desde el cuerpo JSON de la solicitud
        stats = StatsModel(**stats_data)
        
        player.stats.append(stats)
        db.session.add(stats)
        db.session.add(player)
        db.session.commit()
        return player