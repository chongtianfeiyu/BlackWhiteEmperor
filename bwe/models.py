from uuid import uuid4

class Player:
    fieldList = ["id", "playerName"]
    def __init__(self, playerName):
        self.id = uuid4()
        self.playerName = playerName
        self.cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def attent(self, game):
        game.add_player(self)

class Game:
    fieldList = ["id", "gameName", "players"]
    def __init__(self, gameName, owner):
        self.id = uuid4()
        self.gameName = gameName
        self.players = [owner]

    def start(self):
        self.__init_cards()
        self.__deal()

    def __init_cards(self):
        self.cards = [4, 4, 4, 4, 4, 4, 12, 12, 24] # bk wk br wr ba wa s m f

    def __deal(self):
        return

    def add_player(self, player):
        self.players.append(player)