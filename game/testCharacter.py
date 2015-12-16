import unittest
from character import *

class testCharacter(unittest.TestCase):
    def test_basic(self):
        c = Character("John")

    def test_hurt(self):
        c = Character("John")
        self.assertTrue(c.is_alive())
        c.hurt(c.hp()/2)
        self.assertTrue(c.is_alive())
        c.hurt(c.hp() + 1)
        self.assertFalse(c.is_alive())

    def test_heal(self):
        c = Character("John")
        base_hp = c.hp()
        hp = c.hp()
        c.hurt(hp/2)
        c.heal(hp)

        self.assertEqual(c.hp(), base_hp)


    def test_exp(self):
        c = Character("Winnter")

        self.assertEqual(c.hp(), 100)
        self.assertEqual(c.base_hp(), 100)

        c.won()

        self.assertEqual(c.hp(), 100)
        self.assertEqual(c.base_hp(), 100)

        c.won()

        self.assertEqual(c.hp(), 100)
        self.assertEqual(c.base_hp(), 106)

        c.won()
        c.won()
        c.won()
        c.won()

        self.assertEqual(c.hp(), 100)
        self.assertEqual(c.base_hp(), 115)
        

