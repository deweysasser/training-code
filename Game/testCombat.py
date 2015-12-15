import unittest
from Character import *
from Combat import *


class testCombat(unittest.TestCase):
    def test_basic(self):
        c1 = Character("John", hp=100)
        c2 = Character("James", hp=50)

        combat = Combat(c1, c2)

        combat.exchange()

        self.assertTrue(c2.hp() < 50)
