import json
from bwe.lobby import app
from bwe.utils.authentication import oauth
@app.route("/lobby/players", methods=["GET"])
@oauth
def list_all_players_in_lobby(player):
    return json.dumps([1,2,3,4,5]), 200

@app.route("/lobby/player_online", methods=["PUT"])
@oauth
def player_enter_lobby(player):
    return json.dumps(player), 200

@app.route("/lobby/player_offline", methods=["PUT"])
@oauth
def player_leave_lobby(player):
    return json.dumps(player), 200
