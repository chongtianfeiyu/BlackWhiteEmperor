from uuid import uuid4

class Player:
    fieldList = ["id", "playerName", "cards"]
    def __init__(self, playerName):
        self.id = uuid4()
        self.playerName = playerName
        self.game = None
        self.init_cards()

    def init_cards(self):
        self.cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cardSum = 0;


    def attend(self, game):
        self.game = game
        game.players.append(self)

    def exchange(self, targetPlayer, originCardType, targetCardType):
        self.cards[originCardType] -= 1
        self.cards[targetCardType] += 1
        targetPlayer.cards[originCardType] += 1
        targetPlayer.cards[targetCardType] -= 1

    def pickup_card(self, cardType):
        self.cards[cardType] += 1
        self.cardSum += 1
        self.game.cards[cardType] -= 1
        self.game.cardSum -= 1
        
    def reinforce(self,targetPlayer, cardType):
        self.cards[cardType] -= 1
        self.cardSum -= 1
        targetPlayer.cards[cardType] += 1

    def attack(self, targetPlayer, originCards, targetCards):
        return

    def card_count(self):
        return self.cardSum

class Game:
    fieldList = ["id", "gameName", "players", "cards"]
    def __init__(self, gameName, owner):
        self.id = uuid4()
        self.gameName = gameName
        self.players = [owner]
        owner.game = self
        self.__init_cards()

    def start(self):
        self.__init_cards()
        self.__deal()

    def __init_cards(self):
        self.cards = [1, 1, 4, 4, 4, 4, 4, 4, 12, 12, 24] # be we bk wk br wr ba wa s m f
        self.cardSum = 74;
        for player in self.players:
            player.init_cards()

    def __deal(self):
        from random import randint
        if len(self.players) > 2:# Pickup The Black/White Empirors
            for cardType in range(2):
                self.players[randint(0,len(self.players)-1)].pickup_card(cardType)
        elif len(self.players) == 2:
            # Give the Black Empiror to the first player and the White Empiror to the second player
            self.players[0].pickup_card(0)
            self.players[1].pickup_card(1)

        self.cardSum -= 2

        for player in self.players:
            while player.card_count() < 12:
                cardNum = randint(1, self.cardSum-1)
                cardType = 2
                while cardNum - self.cards[cardType] > 0:
                    cardNum -= self.cards[cardType]
                    cardType += 1

                player.pickup_card(cardType)