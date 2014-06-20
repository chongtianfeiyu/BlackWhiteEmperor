#!/usr/bin/env python
# coding=utf-8


import json
from flask import request
from bwe.lobby import app

@app.route("/lobby/players", methods=["GET"])
def list_all_players_in_lobby():
    return json.dumps([1,2,3,4,5]), 200

@app.route("/lobby/player_online", methods=["PUT"])
def player_enter_lobby():
    player = request.json
    return json.dumps(player), 200

@app.route("/lobby/player_offline", methods=["PUT"])
def player_leave_lobby():
    player = request.json
    return json.dumps(player), 200
