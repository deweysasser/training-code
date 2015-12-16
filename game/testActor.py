import unittest

from actor import *
from item import *

class testActor(unittest.TestCase):
    def test_attack_weight(self):
        a = Actor("test");

        self.assertEqual(0, a.attack_weight())

        a.add_item(Item("Something", attack_weight=10))
        a.add_item(Item("Something else", attack_weight=5))
        a._attack_weight = 2

        self.assertEqual(17, a.attack_weight())
        
