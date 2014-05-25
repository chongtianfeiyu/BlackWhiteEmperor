from bwe.lobby import app
import bwe.lobby.blueprints
from flaskext.actions import Manager

manager = Manager(app, default_server_actions=True)
if __name__ == "__main__":
    manager.run()
