from flask import Flask, redirect
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from resources.Player import blp as player_blp
from resources.Team import blp as team_blp
from resources.Coach import blp as coach_blp

from db import db
import models

load_dotenv()  # Cargar variables de entorno desde un archivo .env

def create_app(db_url=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url or os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['API_TITLE'] = 'Basketball Players'
    app.config['API_VERSION'] = 'v1'
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


    db.init_app(app)
    migrate = Migrate(app, db)

    api = Api(app)

    api.register_blueprint(player_blp)
    api.register_blueprint(team_blp)
    api.register_blueprint(coach_blp)

    return app