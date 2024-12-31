import os
from flask import Flask, request, jsonify
from flask_smorest import Api, Blueprint, abort
from flask_migrate import Migrate
from dotenv import load_dotenv

from resources.Player import blp as PlayerBlueprint
from resources.Team import blp as TeamBlueprint
from resources.Stat import blp as StatBlueprint
from resources.Tournament import blp as TournamentBlueprint

from db import db

import models

app = Flask(__name__)

def create_app(db_url=None):
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = db_url or os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['API_TITLE'] = 'Basketball Players'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.2'
    app.config['OPENAPI_URL_PREFIX'] = '/openapi'
    app.config['OPENAPI_REDOC_PATH'] = '/redoc'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    app.config['OPENAPI_REDOC_URL'] = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'

    db.init_app(app)
    migrate = Migrate(app, db)

    api = Api(app)

    api.register_blueprint(PlayerBlueprint)
    api.register_blueprint(TeamBlueprint)
    api.register_blueprint(StatBlueprint)

    return app