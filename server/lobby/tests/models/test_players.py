#!/usr/bin/env python
# coding=utf-8


import unittest, time, md5
from bwe.lobby.models.entities import Player

class PlayersTest(unittest.TestCase):

    def test_create(self):
        PASSES = 32768
        def gen_hash(password, salt=None):
            salt = md5.md5(str(time.time())).hexdigest()
            comp = salt + password
            out = md5.md5(comp).hexdigest()
            for i in xrange(PASSES-1):
                out = md5.md5(out + comp).hexdigest()
            return salt, out

        player = Player(name=u'rothcold2')
        player.salt, player.password = gen_hash(u"123456")
        player.save()

if __name__ == "__main__":
    unittest.main()
