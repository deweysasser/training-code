import unittest
from character import *
from combat import *
from item import *


class testCombat(unittest.TestCase):

    def test_random(self):
        ''' Verify that random works they way I believe it does'''
        combat = Combat(None, None, seed=0)

        self.assertEquals(combat.random.randrange(0, 100), 84)
        self.assertEquals(combat.random.randrange(0, 100), 75)
        self.assertEquals(combat.random.randrange(0, 100), 42)

    def test_basic(self):
        ''' test basic combat functionality '''
        c1 = Character("John", hp=15)
        c2 = Character("James", hp=10)
        d = [7, 0, 0, 0, 0, 3, 0, 0, 5]

        combat = Combat(c1, c2, seed=0)

        combat.fight()

        self.assertEquals(len(combat.history), 9)
        results = [x[0] for x in combat.history]

        self.assertEquals(results, d)
        self.assertTrue(c1.is_alive())
        self.assertFalse(c2.is_alive())
        self.assertEquals(c1.hp(), 12)
        

    def test_bfg(self):
        ''' test basic combat functionality '''
        c1 = Character("John", hp=15)
        c2 = Character("James", hp=10)

        c2.add_item(Item("Sword", attack_damage = 10))

        d = [7, 0, 0, 0, 0, 13, 0, 0, 5]

        combat = Combat(c1, c2, seed=0)

        combat.fight()

        self.assertEquals(len(combat.history), 9)
        results = [x[0] for x in combat.history]

        self.assertEquals(results, d)
        self.assertTrue(c1.is_alive())
        self.assertFalse(c2.is_alive())
        self.assertEquals(c1.hp(), 2)


