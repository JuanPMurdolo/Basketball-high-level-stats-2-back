from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PlayerSchema, PlainStatSchema
from models import Player, Stat

blp = Blueprint('players', 'players', url_prefix='/players')

@blp.route('/')
class Players(MethodView):
    @blp.response(PlayerSchema(many=True))
    def get(self):
        players = Player.query.all()
        return players

    @blp.arguments(PlayerSchema)
    @blp.response(PlayerSchema)
    def post(self, new_data):
        player = Player(**new_data)
        player.save()
        return player
    

@blp.route('/<int:id>')
class PlayerById(MethodView):
    @blp.response(PlayerSchema)
    def get(self, id):
        player = Player.query.get_or_404(id)
        return player

    @blp.arguments(PlayerSchema)
    @blp.response(PlayerSchema)
    def put(self, new_data, id):
        player = Player.query.get_or_404(id)
        player.update(**new_data)
        return player

    @blp.response(code=204)
    def delete(self, id):
        player = Player.query.get_or_404(id)
        player.delete()
        return None
    
#Create a new stat for a player
#Update a stat for a player
#Delete a stat for a player
@blp.route('/<int:id>/stats', methods=['POST'])
class CreatePlayerStat(MethodView):
    @blp.arguments(PlainStatSchema)
    @blp.response(PlayerSchema)
    def post(self, new_stat, id):
        player = Player.query.get_or_404(id)
        player.stats.append(new_stat)
        player.save()
        return player.stats[-1]


@blp.route('/<int:id>/stats/<int:stat_id>', methods=['PUT'])
class UpdatePlayerStat(MethodView):
    @blp.arguments(PlainStatSchema)
    @blp.response(PlayerSchema)
    def put(self, updated_stat, id, stat_id):
        player = Player.query.get_or_404(id)
        if stat_id >= len(player.stats):
            abort(404, message="Stat not found")
        player.stats[stat_id] = updated_stat
        player.save()
        return player.stats[stat_id]


@blp.route('/<int:id>/stats/<int:stat_id>', methods=['DELETE'])
class DeletePlayerStat(MethodView):
    @blp.response(code=204)
    def delete(self, id, stat_id):
        player = Player.query.get_or_404(id)
        if stat_id >= len(player.stats):
            abort(404, message="Stat not found")
        player.stats.pop(stat_id)
        player.save()
        return None