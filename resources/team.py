from datetime import datetime
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import PlayerSchema, StatsSchema, TeamSchema
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models.team import Team as TeamModel
from models.player import Player as PlayerModel
from models.stats import Stats as StatsModel
from models.game import Game as GameModel

blp = Blueprint(
    "teams", __name__, url_prefix="/teams", description="Operations on teams"
)

@blp.route("/<int:team_id>")
class Team(MethodView):
    @blp.response(200, TeamSchema)
    def get(self, team_id: int):
        try:
            team = TeamModel.query.get_or_404(team_id)
            return team
        except KeyError:
            abort(404, message="Team doesn't exist")


@blp.route("")
class Teams(MethodView):
    @blp.arguments(TeamSchema)
    @blp.response(201, TeamSchema)
    def post(self, team_data):
        team = TeamModel(**team_data)
        try:
            db.session.add(team)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()  # Rollback the transaction on error
            abort(500, message="Database error: " + str(e))

    @blp.arguments(TeamSchema)
    @blp.response(200, TeamSchema)
    def put(self, team: dict, team_id: str):
        try:
            team = TeamModel.query.get_or_404(team_id)
            return team
        except KeyError:
            abort(404, message="Team doesn't exist")

    @blp.response(200, TeamSchema(many=True))
    def get(self):
        return TeamModel.query.all()
    
@blp.route("/<int:team_id>/player/<int:player_id>")
class Team(MethodView):
    @blp.response(200, PlayerSchema)
    def get(self, team_id: str, player_id: str):
        try:
            
            #return teams[team_id]
            return None
        except KeyError:
            abort(404, message="Team {team_id} doesn't exist")

@blp.route("/<int:team_id>/players/")
class Team(MethodView):
    @blp.response(200, PlayerSchema(many=True))
    def get(self, team_id: str):
        try:
            team = TeamModel.query.get_or_404(team_id)
            return team.players
        except KeyError:
            abort(404, message="Team {team_id} doesn't exist")

    @blp.arguments(PlayerSchema)
    @blp.response(200, PlayerSchema)
    def post(self,player_data, team_id):
        team = TeamModel.query.get_or_404(team_id)
        if team is None:
            abort(404, message="Team doesn't exist")
        player = PlayerModel(**player_data)
        #player.date_of_birth = datetime.strptime(player_data["date_of_birth"], '%m-%d-%Y').date()
        team.players.append(player)
        try:
            db.session.add(team)
            db.session.add(player)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return team
    
@blp.route("/<int:team_id>/game/<int:game_id>/local/stats")
class Team(MethodView):
    @blp.arguments(StatsSchema)
    @blp.response(200, StatsSchema)
    def patch(self, stats_data, team_id, game_id):
        team = TeamModel.query.get_or_404(team_id)
        if team is None:
            abort(404, message="Team doesn't exist")
        stats = StatsModel(**stats_data)
        game = GameModel.query.get_or_404(game_id)
        if game is None:
            abort(404, message="Game doesn't exist")
        team.stats.append(stats)
        game.local_team_stats.append(stats)
        try:
            db.session.add(game)
            db.session.add(stats)
            db.session.add(team)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")

@blp.route("/<int:team_id>/game/<int:game_id>/visitor/stats")
class Team(MethodView):
    @blp.arguments(StatsSchema)
    @blp.response(200, StatsSchema)
    def patch(self, stats_data, team_id, game_id):
        team = TeamModel.query.get_or_404(team_id)
        if team is None:
            abort(404, message="Team doesn't exist")
        stats = StatsModel(**stats_data)
        game = GameModel.query.get_or_404(game_id)
        if game is None:
            abort(404, message="Game doesn't exist")
        team.stats.append(stats)
        game.visitor_team_stats.append(stats)
        try:
            db.session.add(stats)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")

