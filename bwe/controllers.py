#!/usr/bin/env python
#encoding:utf-8
from models import *
import web


class BaseController:
    def __init__(self):
        self.url_parts = web.ctx.path.split('/')
        self.data = web.data()
        if len(self.url_parts) > 2:
            self.id = self.url_parts[2]
        web.ctx.session.start()

    def GET(self):
        if not self.id is None:
            return self.list()
        else:
            return self.show()

    def POST(self):
        if not self.data["do"] is None:
            action = getattr(obj, self.data["do"])
            return action()
        return True


class GameController(BaseController):
    def __init__(self):
        super(GameController, self).__init__(self)
        if not self.id is None:
            self.game = find_by_id(self.id, games)

    def list(self):
        return build_list_json(games)

    def show(self):
        return build_single_json(self.game)

    def new(self):
        player = web.ctx.session["player"]
        games.append(Game(player))
        return True

    def start(self):
        if self.game.start():
            return "success"
        else:
            return "fail"


class PlayerController(BaseController):
    def __init__(self):
        super(PlayerController, self).__init__()
        if not self.id is None:
            self.player = find_by_id(self.id, players)

    def list(self):
        return build_list_json(players)

    def show(self):
        return build_single_json(self.player)

    def new(self):
        player = Player(self.data["playerName"])
        players.append(player)
        web.ctx.session["currentPlayer"] = player
        web.ctx.session.save()
        return build_single_json(player)

    def attend_game(self):
        player = web.ctx.session["currentPlayer"]
        game = find_by_id(self.data["gameId"], games)
        game.players.append(player)
        web.ctx.session["currentGame"] = game
        web.ctx.session.save()
        return build_single_json(game)

    def quit_game(self):
        game = web.ctx.session["currentGame"]
        game.players = filter(lambda player: player.id != self.id, game.players)
        return "success"

    def exchange(self):
        game = find_by_id(self.data["gameId"])
        targetPlayer = find_by_id(self.data["targetPlayerId"])
        originCardType = self.data["originCardType"]
        targetCardType = self.data["targetCardType"]
        web.ctx.session["currentPlayer"].exchange(targetPlayer, originCardType, targetCardType)
        return "success"

    def pick_card(self):
        cardType = self.data["cardType"]
        web.ctx.session["currentPlayer"].pickup_card(cardType)
        web.ctx.session["currentGame"].card_be_picked(cardType)
        return "success"

    def reinforce(self):
        cardType = self.data["cardType"]
        targetPlayer = find_by_id(self.data["targetPlayerId"])
        web.ctx.session["currentPlayer"].reinforce(targetPlayer, cardType)
        return "success"

    def attack(self):
        return True
