#!/usr/bin/env python
# coding=utf-8


import sys

reload(sys)
sys.setdefaultencoding('UTF-8')


import tests
from bwe.lobby import app
import bwe.utils.filters
import bwe.lobby.blueprints
from flaskext.actions import Manager

manager = Manager(app, default_server_actions=True)

@manager.register("runtest")
def run_tests(application):
    def action(t=('t', 'all')):
        tests.run_tests(t)
    return action

if __name__ == "__main__":
    import bwe.lobby.models.players
    manager.run()
