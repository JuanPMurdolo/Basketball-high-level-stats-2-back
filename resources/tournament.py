from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
import sqlalchemy
from schemas import GameSchema, GamesTesting, TournamentSchema
from models.tournament import Tournament as TournamentModel
from models.game import Game as GameModel
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

@blp.route("/<int:tournament_id>/game")
class Tournament(MethodView):
    @blp.arguments(GamesTesting)
    @blp.response(200, TournamentSchema)
    def post(self, game_info, tournament_id):
        tournament = TournamentModel.query.get_or_404(tournament_id)
        try:
            game = GameModel(**game_info)
            tournament.games.append(game)
            db.session.add(game)
            db.session.add(tournament)
            db.session.commit()
            return tournament
        except sqlalchemy.exc.IntegrityError as e:
            db.session.rollback()  # Rollback the transaction
            error_message = str(e)
            # Log the error message and potentially handle the error gracefully
            print("Error creating game:", error_message)
            abort(500, message="Error al crear el torneo")
