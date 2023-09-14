import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from models.player import Player as PlayerModel
from models.team import Team as TeamModel
from models.game import Game as GameModel
from schemas import BaseGameSchema, GameSchema
from .funciones import *
from db import db

blp = Blueprint(
    "games", __name__, url_prefix="/games", description="Operations on games"
)

@blp.route("/<int:game_id>")
class Game(MethodView):
    @blp.response(200, GameSchema)
    def get(self, game_id):
        try:
            game = Game.query.get_or_404(game_id)
            return game
        except KeyError:
            abort(404, message="Game doesn't exist")

    @blp.arguments(GameSchema)
    @blp.response(200, GameSchema)
    def patch(self, game_info, game_id):
        game = Game.query.get_or_404(game_id)
        localTeam = game.local_team
        visitorTeam = game.visitor_team
        local_team_stats = game_info["local_team_stats"]
        localTeam.stats.append(local_team_stats)
        visitor_team_stats = game_info["visitor_team_stats"]
        visitorTeam.stats.append(visitor_team_stats)
        local_players_stats = game_info["local_players_stats"]

        for player_stats in local_players_stats:
            player_id = player_stats["player_id"]
            stats = player_stats["stats"]
            player = PlayerModel.query.get_or_404(player_id)
            player.stats.append(stats)
            try:
                db.session.save(player)
                db.session.commit()
            except:
                abort(500, message="Error al actualizar las estadísticas del jugador")
        visitor_players_stats = game_info["visitor_players_stats"]
        for visitor_stats in visitor_players_stats:
            player_id = visitor_stats["player_id"]
            stats = visitor_stats["stats"]
            player = PlayerModel.query.get_or_404(player_id)
            player.stats.append(stats)
            try:
                db.session.save(player)
                db.session.commit()
            except:
                abort(500, message="Error al actualizar las estadísticas del jugador")
        sumarEstadisticas(game)
        try:
            db.session.save(game)
            db.session.commit()
        except:
            abort(500, message="Error al actualizar las estadísticas del equipo")
        return game


@blp.route("")
class Games(MethodView):
    @blp.arguments(BaseGameSchema)
    @blp.response(201, BaseGameSchema)
    def post(self, game_data):
        game = {**game_data}
        print(game)
        visitor_team_id = game["visitor_team_id"]
        local_team_id = game["local_team_id"]
        local_team = TeamModel.query.get_or_404(local_team_id)
        visitor_team = TeamModel.query.get_or_404(visitor_team_id)
        game["local_team_name"] = local_team.name
        game["visitor_team_name"] = visitor_team.name
        game["court"] = local_team.court
        print(game)
        try:
            db.session.add(game)
            db.session.commit()
        except:
            abort(500, message="Error al crear el partido")        
        return game
    
    @blp.response(200, GameSchema(many=True))
    def get(self):
        return GameModel.query.all()
    
