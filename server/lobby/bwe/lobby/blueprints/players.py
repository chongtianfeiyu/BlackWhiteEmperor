#!/usr/bin/env python
# coding=utf-8


import json, uuid
from flask import request
from bwe.lobby import app

@app.route("/players/<player_id>", methods=["GET"])
def get_player(player_id):
    return player_id, 200

@app.route("/players", methods=["POST"])
def create_player(player_id):
    return json.dumps({"player_id": 1}), 201

@app.route("/login", methods=["PUT"])
def login():
    return json.dumps({"token": str(uuid.uuid1())}), 200

@app.route("/logout", methods=["PUT"])
def logout():
    player = request.json
    return json.dumps(player), 200
