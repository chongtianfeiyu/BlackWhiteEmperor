#!/usr/bin/env python
#encoding:utf-8

class BaseController:
    def __init__(self):
        self.url_parts = web.ctx.path.split('/')
        self.data = web.data()
        if len(self.url_parts) > 2:
          self.id = self.url_parts[2]

    def GET(self):
        if not self.id is None:
          return self.list()
        else:
          return self.show()

    def POST(self):
        if not self.data["do"] is None
          action = getattr(obj, self.data["do"])
          return action()
        return 

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
        playerId = self.data["playerId"]
        player = find_player(playerId)
        games.append(Game(player))

    def attend(self):
        playerId = self.data["playerId"]

    def start(self):
        if self.game.start():
            return "success"
        else:
            return "fail"


class PlayerController(BaseController):
    def list(self):
        return build_list_json(players)

    def attack(self):
        return

    def pick_card(type):
        return
