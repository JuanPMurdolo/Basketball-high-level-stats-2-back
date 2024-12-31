from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PlainStatSchema
from models import Stat, Player

blp = Blueprint('stats', 'stats', url_prefix='/stats')

@blp.route('/')

class Stats(MethodView):
    @blp.response(PlainStatSchema(many=True))
    def get(self):
        stats = Stat.query.all()
        return stats

    @blp.arguments(PlainStatSchema)
    @blp.response(PlainStatSchema)
    def post(self, new_data):
        stat = Stat(**new_data)
        stat.save()
        return stat
    
@blp.route('/<int:id>')
class StatById(MethodView):
    @blp.response(PlainStatSchema)
    def get(self, id):
        stat = Stat.query.get_or_404(id)
        return stat

    @blp.arguments(PlainStatSchema)
    @blp.response(PlainStatSchema)
    def put(self, new_data, id):
        stat = Stat.query.get_or_404(id)
        stat.update(**new_data)
        return stat

    @blp.response(code=204)
    def delete(self, id):
        stat = Stat.query.get_or_404(id)
        stat.delete()
        return None
    
#Create a new stat for a player
#Update a stat for a player
#Delete a stat for a player
@blp.route('/<int:id>/stats', methods=['POST'])
class CreatePlayerStat(MethodView):
    @blp.arguments(PlainStatSchema)
    @blp.response(PlainStatSchema)
    def post(self, new_stat, id):
        player = Player.query.get_or_404(id)
        player.stats.append(new_stat)
        player.save()
        return player.stats[-1]
    
@blp.route('/<int:id>/stats/<int:stat_id>', methods=['PUT'])
class UpdatePlayerStat(MethodView):
    @blp.arguments(PlainStatSchema)
    @blp.response(PlainStatSchema)
    def put(self, updated_stat, id, stat_id):
        player = Player.query.get_or_404(id)
        player.stats[stat_id] = updated_stat
        player.save()
        return player.stats[stat_id]

@blp.route('/<int:id>/stats/<int:stat_id>', methods=['DELETE'])
class DeletePlayerStat(MethodView):
    @blp.response(code=204)
    def delete(self, id, stat_id):
        player = Player.query.get_or_404(id)
        player.stats.pop(stat_id)
        player.save()
        return None