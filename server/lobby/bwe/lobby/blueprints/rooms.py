import json
from bwe.lobby import app

@app.route("/rooms/<room_id>", methods=["GET"])
def get_room(room_id):
    return room_id, 200

@app.route("/rooms/<room_id>/invite_player/<player_id>", methods=["PUT"])
def invite_player_into_room(room_id, player_id):
    return "%s : %s" % (room_id, player_id), 200

@app.route("/rooms/<room_id>/kickout_player/<player_id>", methods=["PUT"])
def kickout_player_from_room(room_id, player_id):
    return "%s : %s" % (room_id, player_id), 200


@app.route("/rooms/<room_id>/enter", methods=["PUT"])
def player_enter_room(room_id):
    return room_id, 200

@app.route("/rooms/<room_id>/leave", methods=["PUT"])
def player_leave_room(room_id):
    return room_id, 200

@app.route("/rooms", methods=["GET"])
def list_rooms():
    return json.dumps([]), 200

@app.route("/rooms", methods=["POST"])
def create_room():
    return json.dumps({"room_id": 1}), 201
