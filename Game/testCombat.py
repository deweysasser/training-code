import unittest
from Character import *
from Combat import *


class testCombat(unittest.TestCase):

    def test_random(self):
        combat = Combat(None, None, seed=0)

        self.assertEquals(combat.random.randrange(0, 100), 84)
        self.assertEquals(combat.random.randrange(0, 100), 75)
        self.assertEquals(combat.random.randrange(0, 100), 42)

    def test_basic(self):
        c1 = Character("John", hp=15)
        c2 = Character("James", hp=10)
        d = [7, 0, 0, 0, 0, 3, 0, 0, 5]

        combat = Combat(c1, c2, seed=0)

        combat.fight()

        self.assertEquals(len(combat.history), 9)
        results = [x[0] for x in combat.history]

        self.assertEquals(results, d)

