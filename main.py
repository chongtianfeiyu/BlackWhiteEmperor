#!/usr/bin/env python
#coding:UTF-8

import web
from bwe import *

games = []
players = []

urls = ("/game/.*", "GameController",
        "/player/*", "PlayerController")

app = web.application(urls, globals())


if __name__ == "__main__":
    # web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()