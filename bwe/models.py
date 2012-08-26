from uuid import uuid4

class Player:
    fieldList = ["id", "playerName", "cards"]
    def __init__(self, playerName):
        self.id = uuid4()
        self.playerName = playerName
        self.cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def attent(self, game):
        game.add_player(self)

    def exchange(self, targetPlayer, originCardType, targetCardType):
        self.cards[originCardType] -= 1
        self.cards[targetCardType] += 1
        targetPlayer.cards[originCardType] += 1
        targetPlayer.cards[targetCardType] -= 1

    def pickup_card(self, cardType):
        self.cards[cardType] += 1
    def reinforce(self,targetPlayer, cardType):
        self.cards[cardType] -= 1
        targetPlayer.cards[cardType] += 1

class Game:
    fieldList = ["id", "gameName", "players", "cards"]
    def __init__(self, gameName, owner):
        self.id = uuid4()
        self.gameName = gameName
        self.players = [owner]
        self.__init_cards()

    def start(self):
        self.__init_cards()
        self.__deal()

    def __init_cards(self):
        self.cards = [4, 4, 4, 4, 4, 4, 12, 12, 24] # bk wk br wr ba wa s m f

    def __deal(self):
        return

    def add_player(self, player):
        self.players.append(player)

    def card_be_picked(self, cardType):
        self.cards[cardType] -= 1
