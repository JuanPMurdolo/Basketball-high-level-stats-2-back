from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PlayerSchema, TeamSchema
from models import Team, Player

blp = Blueprint('teams', 'teams', url_prefix='/teams')

@blp.route('/')
class Teams(MethodView):
    @blp.response(TeamSchema(many=True))
    def get(self):
        teams = Team.query.all()
        return teams

    @blp.arguments(TeamSchema)
    @blp.response(TeamSchema)
    def post(self, new_data):
        team = Team(**new_data)
        team.save()
        return team
    
    @blp.route('/<int:team_id>/players')
    class Players(MethodView):
        @blp.response(PlayerSchema(many=True))
        def get(self, team_id):
            team = Team.query.get_or_404(team_id)
            players = team.players
            return players

        @blp.arguments(PlayerSchema)
        @blp.response(PlayerSchema, code=201)
        def post(self, new_data, team_id):
            team = Team.query.get_or_404(team_id)
            player = Player(**new_data)
            team.players.append(player)
            team.save()
            return player, 201

    @blp.route('/<int:team_id>/players/<int:player_id>')
    class Player(MethodView):
        @blp.response(PlayerSchema)
        def get(self, team_id, player_id):
            team = Team.query.get_or_404(team_id)
            player = team.players.filter_by(id=player_id).first_or_404()
            return player

        @blp.arguments(PlayerSchema)
        @blp.response(PlayerSchema)
        def put(self, new_data, team_id, player_id):
            team = Team.query.get_or_404(team_id)
            player = team.players.filter_by(id=player_id).first_or_404()
            player.update(**new_data)
            team.save()
            return player

        @blp.response(code=204)
        def delete(self, team_id, player_id):
            team = Team.query.get_or_404(team_id)
            player = team.players.filter_by(id=player_id).first_or_404()
            player.delete()
            team.save()
            return '', 204