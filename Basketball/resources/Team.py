import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import TeamSchema
from db import teams

blp = Blueprint(
    "teams", __name__, url_prefix="/teams", description="Operations on teams"
)

@blp.route("/<string:team_id>")
class Team(MethodView):
    @blp.response(200, TeamSchema)
    def get(self, team_id: str):
        try:
            return teams[team_id]
        except KeyError:
            abort(404, message="Team {team_id} doesn't exist")

@blp.route("")
class Teams(MethodView):
    @blp.arguments(TeamSchema)
    @blp.response(201, TeamSchema)
    def post(self, team_data):
        team_id = uuid.uuid4().hex
        team = {**team_data, "id": team_id}
        teams[team_id] = team        
        return team

    @blp.arguments(TeamSchema)
    @blp.response(200, TeamSchema)
    def put(self, team: dict, team_id: str):
        try:
            teams[team_id] = team
            return team
        except KeyError:
            abort(404, message="Team doesn't exist")

    @blp.response(200, TeamSchema(many=True))
    def get(self):
        return list(teams.values())