from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import GameSchema, TournamentSchema
from models.tournament import Tournament as TournamentModel
from db import db

blp = Blueprint(
    "tournaments", __name__, url_prefix="/tournaments", description="Operations on tournaments"
)

@blp.route("/<int:id>")
class Tournament(MethodView):
    @blp.response(200, TournamentSchema)
    def get(self, id):
        try:
            tournament = Tournament.query.get_or_404(id)
            return tournament
        except KeyError:
            abort(404, message="Tournament {season} doesn't exist")


@blp.route("")
class Tournament(MethodView):
    @blp.arguments(TournamentSchema)
    @blp.response(200, TournamentSchema)
    def post(self, tournament_info):
        tournament = TournamentModel(**tournament_info)
        try:
            db.session.add(tournament)
            db.session.commit()
            return tournament
        except:
            abort(500, message="Error al crear el torneo")

@blp.route("/game/")
class Tournament(MethodView):
    @blp.arguments(GameSchema)
    @blp.response(200, GameSchema)
    def post(self, game_info):
        tournament_id = game_info["tournament_id"]
        tournament = TournamentModel.query.get_or_404(tournament_id)
        tournament.games.append(game_info)
        try:
            db.session.save(tournament)
            db.session.commit()
            return tournament
        except:
            abort(500, message="Error al crear el torneo")
