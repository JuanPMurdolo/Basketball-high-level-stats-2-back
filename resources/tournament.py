from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import TournamentSchema

blp = Blueprint(
    "tournaments", __name__, url_prefix="/tournaments", description="Operations on tournaments"
)

@blp.route("/tournaments/<string:season>")
class Tournament(MethodView):
    @blp.response(200, TournamentSchema)
    def get(self, season: str):
        try:
            #return tournaments[season]
            return None
        except KeyError:
            abort(404, message="Tournament {season} doesn't exist")