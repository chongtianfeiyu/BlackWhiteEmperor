#!/usr/bin/env python
#encoding:utf-8
import sys
sys.path.append("..")

from bwe.models import *
import unittest
import random


class TestModelFunctions(unittest.TestCase):
    def init_game(self):
        self.game = Game("Test Room", Player("Tom"))
        Player("Jim").attend(self.game)

    def test_attend(self):
        self.init_game()
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.players[1].playerName, "Jim")

    def test_exchange(self):
        self.init_game()
        players = self.game.players
        cardType1 = random.randint(2, len(players[0].cards)-1)
        cardType2 = random.randint(2, len(players[1].cards)-1)
        players[0].pickup_card(cardType1)
        players[1].pickup_card(cardType2)
        self.assertEqual(players[0].cards[cardType1], 1)
        self.assertEqual(players[1].cards[cardType2], 1)
        players[0].exchange(players[1], cardType1, cardType2)
        self.assertEqual(players[0].cards[cardType2], 1)
        self.assertEqual(players[1].cards[cardType1], 1)

    def test_pickup_card(self):
        self.init_game()
        player = self.game.players[0]
        cards = [4, 4, 4, 4, 4, 4, 12, 12, 24]
        for i in range(len(cards)):
            cards[i] = random.randint(0, cards[i])
        for i in range(len(cards)):
            for j in range(cards[i]):
                player.pickup_card(i)
        for i in range(len(cards)):
            self.assertEqual(player.cards[i], cards[i])

    def test_reinforce(self):
        self.init_game()
        players = self.game.players
        players[0].pickup_card(0)
        self.assertEqual(players[0].cards[0], 1)
        players[0].reinforce(players[1], 0)
        self.assertEqual(players[0].cards[0], 0)
        self.assertEqual(players[1].cards[0], 1)

    def test_start(self):
        self.init_game()
        self.game.start()
        print("Round 1")
        print(self.game.cards)
        for player in self.game.players:
            print(player.cards)
        Player("Ritch").attend(self.game)
        self.game.start()
        print("Round 2")
        print(self.game.cards)
        for player in self.game.players:
            print(player.cards)

if __name__ == '__main__':
    unittest.main()
