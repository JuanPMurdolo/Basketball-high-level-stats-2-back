import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import GameSchema
from .funciones import *
from db import db

blp = Blueprint(
    "games", __name__, url_prefix="/games", description="Operations on games"
)

@blp.route("/<int:game_id>")
class Game(MethodView):
    @blp.response(200, GameSchema)
    def get(self, game_id: int):
        try:
            #return games[game_id]
            return None
        except KeyError:
            abort(404, message="Game doesn't exist")

    @blp.arguments(GameSchema)
    @blp.response(200, GameSchema)
    def put(self, game: dict, game_id: int):
        try:
            #games[game_id] = game
            return game
        except KeyError:
            abort(404, message="Game doesn't exist")

@blp.route("")
class Games(MethodView):
    @blp.arguments(GameSchema)
    @blp.response(201, GameSchema)
    def post(self, game_data):
        game_id = uuid.uuid4().hex
        game = {**game_data, "id": game_id}
        sumarEstadisticas(game)
        try:
            db.session.add(game)
            db.session.commit()
        except:
            abort(500, message="Error al crear el partido")        
        return game
    
    @blp.response(200, GameSchema(many=True))
    def get(self):
        #return list(games.values())
        return None
    
