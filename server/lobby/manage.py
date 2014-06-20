#!/usr/bin/env python
# coding=utf-8
import config.dev as config
# import config.production as config
from bwe.lobby import app
import bwe.utils.filters
import bwe.lobby.blueprints
from flaskext.actions import Manager

app.config.from_object(config)

manager = Manager(app, default_server_actions=True)
if __name__ == "__main__":
    manager.run()
