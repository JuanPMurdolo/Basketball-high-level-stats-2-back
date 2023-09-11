import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import PlayerSchema

blp = Blueprint(
    "players", __name__, url_prefix="/players", description="Operations on players"
)

@blp.route("/players/<string:player_id>")
class Player(MethodView):
    @blp.response(200, PlayerSchema)
    def get(self, player_id: str):
        try:
            #return players[player_id]
            return None
        except KeyError:
            abort(404, message="Player {player_id} doesn't exist")

@blp.route("/players")
class Players(MethodView):
    @blp.arguments(PlayerSchema)
    @blp.response(201, PlayerSchema)
    def post(self, player_data):
        player_id = uuid.uuid4().hex
        player = {**player_data, "id": player_id}
        #players[player_id] = player        
        return player

    @blp.arguments(PlayerSchema)
    @blp.response(200, PlayerSchema)
    def put(self, player: dict, player_id: str):
        try:
            #players[player_id] = player
            return player
        except KeyError:
            abort(404, message="Player doesn't exist")