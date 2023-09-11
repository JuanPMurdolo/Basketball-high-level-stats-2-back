import os
from flask import Flask,request
from flask_smorest import Api, Blueprint, abort
from resources.game import blp as games_blueprint
from resources.team import blp as teams_blueprint
from resources.tournament import blp as tournaments_blueprint
from resources.player import blp as players_blueprint
from resources.stats import blp as stats_blueprint
from resources.funciones import *
from db import db
import models

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["API_TITLE"] = "Basketball High Level Stats "
    app.config["API_VERSION"] = "v0.1"
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///basketball.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()


    api.register_blueprint(games_blueprint)
    api.register_blueprint(teams_blueprint)
    api.register_blueprint(tournaments_blueprint)
    api.register_blueprint(players_blueprint)
    api.register_blueprint(stats_blueprint)

    return app