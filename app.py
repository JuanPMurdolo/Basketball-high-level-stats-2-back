from flask import Flask,request
from flask_smorest import Api, Blueprint, abort
from Basketball.resources.Game import blp as games_blueprint
from Basketball.resources.Team import blp as teams_blueprint
from Basketball.resources.Tournament import blp as tournaments_blueprint
from Basketball.resources.Player import blp as players_blueprint

app = Flask(__name__)

app.config["API_TITLE"] = "Basketball High Level Stats "
app.config["API_VERSION"] = "v0.1"
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"

api = Api(app)
api.register_blueprint(games_blueprint)
api.register_blueprint(teams_blueprint)
api.register_blueprint(tournaments_blueprint)
api.register_blueprint(players_blueprint)