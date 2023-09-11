import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import PlayerSchema, TeamSchema
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models.team import Team as TeamModel
from models.player import Player as PlayerModel

blp = Blueprint(
    "teams", __name__, url_prefix="/teams", description="Operations on teams"
)

@blp.route("/<int:team_id>")
class Team(MethodView):
    @blp.response(200, TeamSchema)
    def get(self, team_id: int):
        try:
            #return teams[team_id]
            return None
        except KeyError:
            abort(404, message="Team {team_id} doesn't exist")

@blp.route("")
class Teams(MethodView):
    @blp.arguments(TeamSchema)
    @blp.response(201, TeamSchema)
    def post(self, team_data):
        team_id = 1
        team = TeamModel(id=team_id, **team_data)
        try:
            db.session.add(team)
            db.session.commit()
        except:
            abort(500, message="Error al crear el equipo")
        return None

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
        #return list(teams.values())
        return None
    
@blp.route("/<int:team_id>/player/<int:player_id>")
class Team(MethodView):
    @blp.response(200, PlayerSchema)
    def get(self, team_id: str, player_id: str):
        try:
            
            #return teams[team_id]
            return None
        except KeyError:
            abort(404, message="Team {team_id} doesn't exist")

    @blp.arguments(PlayerSchema)
    @blp.response(200, PlayerSchema)
    def post(self,player_data, team_id, player_id):
        team = TeamModel.query.get_or_404(team_id)
        if team is None:
            abort(404, message="Team doesn't exist")
        player = PlayerModel.query.get_or_404(player_id)
        if player is None:
            player = PlayerModel(id=player_id, **player_data)
        else:
            abort(404, message="Player already exist")
        team.players.append(player)
        try:
            db.session.add(team)
            db.session.add(player)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return team

@blp.route("/<int:team_id>/players/")
class Team(MethodView):
    @blp.response(200, PlayerSchema(many=True))
    def get(self, team_id: str):
        try:
            team = TeamModel.query.get_or_404(team_id)
            return team.players
        except KeyError:
            abort(404, message="Team {team_id} doesn't exist")