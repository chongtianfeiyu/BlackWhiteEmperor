import json
from bwe.lobby import app
from bwe.utils.authentication import oauth

@app.route("/rooms/<room_id>", methods=["GET"])
@oauth
def get_room(player, room_id):
    return room_id, 200

@app.route("/rooms/<room_id>/invite_player/<player_id>", methods=["PUT"])
@oauth
def invite_player_into_room(player, room_id, player_id):
    return "%s : %s" % (room_id, player_id), 200

@app.route("/rooms/<room_id>/kickout_player/<player_id>", methods=["PUT"])
@oauth
def kickout_player_from_room(player, room_id, player_id):
    return "%s : %s" % (room_id, player_id), 200


@app.route("/rooms/<room_id>/enter", methods=["PUT"])
@oauth
def player_enter_room(player, room_id):
    return room_id, 200

@app.route("/rooms/<room_id>/leave", methods=["PUT"])
@oauth
def player_leave_room(player, room_id):
    return room_id, 200

@app.route("/rooms", methods=["GET"])
@oauth
def list_rooms(player):
    return json.dumps([]), 200

@app.route("/rooms", methods=["POST"])
@oauth
def create_room(player):
    return json.dumps({"room_id": 1}), 201
