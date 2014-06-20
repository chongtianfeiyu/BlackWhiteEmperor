#!/usr/bin/env python
# coding=utf-8


import lobby, players, rooms
from bwe.lobby import app

@app.route("/token", methods=['POST'])
def generate_token():
    return "{}"
