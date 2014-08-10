#!/usr/bin/env python
# coding=utf-8


from bwe.lobby.models.entities import Player


def __player_key(player_id):
    return "%s:%s" % (Player.__tablename__, player_id)


def get_player(player_id):
    key = __player_key(player_id)
    keys = Player.__table__.columns.keys()
    redis = get_redis()
    values = redis.hmget(key, *keys)
    player = dict(zip(keys, values))
    return player

def create_player(name, password):
    player = Player()
    player.name = name
    player.password = password
    redis = get_redis()
    player_id = redis.incr("player_id")
    keys = Player.__table__.columns.keys()
    key = __player_key(player_id)
    player_dict = {}
    for k in keys:
        player_dict[k] = getattr(player, k)
    redis.hmset(key, player_dict)
    return player.to_dict()

def update_player(player_id, params):
    if params.has_key("name"):
        del params["name"]
    redis = get_redis()
    key = __player_key(player_id)
    redis.hmset(player_id, params)
    return get_player(player_id)
