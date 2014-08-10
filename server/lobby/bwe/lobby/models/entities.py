#!/usr/bin/env python
# coding=utf-8


import rom, time


class Player(rom.Model):
    name = rom.String(required=True, unique=True, suffix=True)
    salt = rom.String()
    password = rom.String()
    played_games = rom.Integer()
    created_at = rom.Float(default=time.time, index=True)


class Room(rom.Model):

    columns = ["id", "name"]

