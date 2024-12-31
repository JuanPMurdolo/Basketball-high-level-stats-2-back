from flask.views import MethodView
from flask_smorest import abort, Blueprint
from flask_jwt_extended import jwt_required
from models.Coach import Coach
from schemas import CoachSchema, PlainCoachSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError
    

blp = Blueprint('coach', 'coach', url_prefix='/coaches')


@blp.route('/')
class CoachList(MethodView):
    @blp.response(200, CoachSchema(many=True))
    def get(self):
        coaches = Coach.query.all()
        return coaches

    @blp.arguments(PlainCoachSchema)
    @blp.response(200, CoachSchema)
    def post(self, new_data):
        coach = Coach(**new_data)
        db.session.add(coach)
        db.session.commit()
        return coach