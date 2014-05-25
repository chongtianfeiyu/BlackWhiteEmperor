import json, uuid
from bwe.lobby import app
from bwe.utils.authentication import oauth

@app.route("/players/<player_id>", methods=["GET"])
@oauth
def get_player(player, player_id):
    return player_id, 200

@app.route("/players", methods=["POST"])
@oauth
def create_player(player, player_id):
    return json.dumps({"player_id": 1}), 201

@app.route("/login", methods=["PUT"])
def login():
    return json.dumps({"token": str(uuid.uuid1())}), 200

@app.route("/logout", methods=["PUT"])
@oauth
def logout(player):
    return json.dumps(player), 200
