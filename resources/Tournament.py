from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import TournamentSchema, TeamSchema
from models import Tournament, Team

blp = Blueprint('tournaments', 'tournaments', url_prefix='/tournaments')

@blp.route('/')
class Tournaments:
    @blp.response(TournamentSchema(many=True))
    def get(self):
        tournaments = Tournament.query.all()
        return tournaments

    @blp.arguments(TournamentSchema)
    @blp.response(TournamentSchema)
    def post(self, new_data):
        tournament = Tournament(**new_data)
        tournament.save()
        return tournament
    
    @blp.route('/<int:tournament_id>/teams')
    class Teams(MethodView):
        @blp.response(TeamSchema(many=True))
        def get(self, tournament_id):
            tournament = Tournament.query.get_or_404(tournament_id)
            teams = tournament.teams
            return teams

        @blp.arguments(TeamSchema)
        @blp.response(TeamSchema, code=201)
        def post(self, new_data, tournament_id):
            tournament = Tournament.query.get_or_404(tournament_id)
            team = Team(**new_data)
            tournament.teams.append(team)
            tournament.save()
            return team, 201
        
    @blp.route('/<int:tournament_id>/teams/<int:team_id>')
    class Team(MethodView):
        @blp.response(TeamSchema)
        def get(self, tournament_id, team_id):
            tournament = Tournament.query.get_or_404(tournament_id)
            team = tournament.teams.filter_by(id=team_id).first_or_404()
            return team

        @blp.arguments(TeamSchema)
        @blp.response(TeamSchema)
        def put(self, new_data, tournament_id, team_id):
            tournament = Tournament.query.get_or_404(tournament_id)
            team = tournament.teams.filter_by(id=team_id).first_or_404()
            team.update(**new_data)
            tournament.save()
            return team

        @blp.response(code=204)
        def delete(self, tournament_id, team_id):
            tournament = Tournament.query.get_or_404(tournament_id)
            team = tournament.teams.filter_by(id=team_id).first_or_404()
            team.delete()
            return None
        