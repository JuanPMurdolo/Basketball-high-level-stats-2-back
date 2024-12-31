from flask.views import MethodView
from flask_smorest import abort, Blueprint
from flask_jwt_extended import jwt_required
from models.Player import Player
from schemas import PlainPlayerSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError


blp = Blueprint('player', 'player', url_prefix='/players')


@blp.route('/')
class PlayerList(MethodView):
    @blp.response(200, PlainPlayerSchema(many=True))
    def get(self):
        players = Player.query.all()
        return players

    @blp.arguments(PlainPlayerSchema)
    @blp.response(200, PlainPlayerSchema)
    def post(self, new_data):
        player = Player(**new_data)
        db.session.add(player)
        db.session.commit()
        return player
    
