from flask.views import MethodView
from flask_smorest import abort, Blueprint
from flask_jwt_extended import jwt_required
from models.Team import Team
from schemas import PlainTeamSchema, TeamSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError


blp = Blueprint('team', 'team', url_prefix='/team')


@blp.route('/')
class PlayerList(MethodView):
    @blp.response(200, TeamSchema(many=True))
    def get(self):
        teams = Team.query.all()
        return teams

    @blp.arguments(PlainTeamSchema)
    @blp.response(200, TeamSchema)
    def post(self, new_data):
        team = Team(**new_data)
        db.session.add(team)
        db.session.commit()
        return team
    
