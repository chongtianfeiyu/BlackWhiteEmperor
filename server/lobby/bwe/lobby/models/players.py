from bwe.lobby.models import get_session
from bwe.lobby.models.entities import Player
class PlayersModel:
    def get_player(self, player_id):
        session = get_session()
        player = session.query(Player).filter(Player.id == player_id).one()
        return player

    def create_player(self, name, password):
        session = get_session()
        player = Player()
        player.name = name
        player.password = password
        session.add(player)

    def update_player(self, player_id, params):
        session = get_session()
        player = session.query(Player).filter(Player.id == player_id).one()
        for key, value in params.iteritems():
            setattr(player, key, value)
        player.save()
