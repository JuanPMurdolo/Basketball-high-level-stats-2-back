import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import GameSchema
from db import games

blp = Blueprint(
    "games", __name__, url_prefix="/games", description="Operations on games"
)

@blp.route("/games/<string:game_id>")
class Game(MethodView):
    @blp.response(200, GameSchema)
    def get(self, game_id: str):
        try:
            return games[game_id]
        except KeyError:
            abort(404, message="Game doesn't exist")

    @blp.arguments(GameSchema)
    @blp.response(200, GameSchema)
    def put(self, game: dict, game_id: str):
        try:
            games[game_id] = game
            return game
        except KeyError:
            abort(404, message="Game doesn't exist")

@blp.route("/games")
class Games(MethodView):
    @blp.arguments(GameSchema)
    @blp.response(201, GameSchema)
    def post(self, game_data):
        game_id = uuid.uuid4().hex
        game = {**game_data, "id": game_id}
        games[game_id] = game        
        return game