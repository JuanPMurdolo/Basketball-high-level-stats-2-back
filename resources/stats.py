import json
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import GameSchema
from .funciones import *

blp = Blueprint(
    "stats", __name__, url_prefix="/stats", description="Operations on stats"
)

@blp.route("/local/<string:game_id>")
class Stats(MethodView):
    @blp.response(200, dict)
    def get(self, game_id: str):
        try:
            #game = games[game_id]
            #stats = dict(game.local_team_stats)
            #return str(callAllFunctions(stats["t2i"], stats["t3i"], stats["t1i"], stats["pp"], stats["puntos"], stats["tcc"], stats["t3c"], stats["tci"], stats["min"], stats["totales"], stats["t1c"], stats["t2c"], stats["t1p"], stats["ro"], stats["asis"]))
            return None
        except KeyError:
            abort(404, message="Game doesn't exist")

@blp.route("/visitor/<string:game_id>")
class Stats(MethodView):
    @blp.response(200, dict)
    def get(self, game_id: str):
        try:
            #game = games[game_id]
            #stats = dict(game.visitor_team_stats)
            #return str(callAllFunctions(stats["t2i"], stats["t3i"], stats["t1i"], stats["pp"], stats["puntos"], stats["tcc"], stats["t3c"], stats["tci"], stats["min"], stats["totales"], stats["t1c"], stats["t2c"], stats["t1p"], stats["ro"], stats["asis"]))
            return None
        except KeyError:
            abort(404, message="Game doesn't exist")

@blp.route("/player/<string:player_id>")
class Stats(MethodView):
    @blp.response(200, dict)
    def get(self, player_id: str):
        #player = players[player_id]
        try:
            #return str(callAllFunctions(player.field_goal_attempts, player.three_point_attempts, player.free_throw_attempts, player.turnovers, player.points, player.field_goals, player.three_pointers, player.free_throws, player.minutes_played, player.total_rebounds, player.free_throws, player.two_pointers, player.free_throw_percentage, player.offensive_rebounds, player.assists))
            return None
        except KeyError:
            abort(404, message="Game doesn't exist")

@blp.route("/<string:game_id>/local/<string:player_id>")
class Stats(MethodView):
    @blp.response(200, dict)
    def get(self, game_id: str, player_id: str):
        try:
            #game = games[game_id]
            #player = dict(game.local_players_stats[player_id])
            #return str(callAllFunctions(player.field_goal_attempts, player.three_point_attempts, player.free_throw_attempts, player.turnovers, player.points, player.field_goals, player.three_pointers, player.free_throws, player.minutes_played, player.total_rebounds, player.free_throws, player.two_pointers, player.free_throw_percentage, player.offensive_rebounds, player.assists))
            return None
        except KeyError:
            abort(404, message="Game doesn't exist")

@blp.route("/<string:game_id>/visitor/<string:player_id>")
class Stats(MethodView):
    @blp.response(200, dict)
    def get(self, game_id: str, player_id: str):
        try:
            #game = games[game_id]
            #player = dict(game.visitor_players_stats[player_id])
            #return str(callAllFunctions(player.field_goal_attempts, player.three_point_attempts, player.free_throw_attempts, player.turnovers, player.points, player.field_goals, player.three_pointers, player.free_throws, player.minutes_played, player.total_rebounds, player.free_throws, player.two_pointers, player.free_throw_percentage, player.offensive_rebounds, player.assists))
            return None
        except KeyError:
            abort(404, message="Game doesn't exist")