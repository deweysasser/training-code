import unittest
from Librarian import *
from Character import *
from Creature import *

class testLibrarian(unittest.TestCase):
    def test_characters(self):
        l = Librarian()
        c1 = Character("John")
        c2 = Character("James")
        l.put_character(c1)
        l.put_character(c2)

        self.assertTrue(l.get_character("John") is not None)
        self.assertTrue(l.get_character("James") is not None)

        self.assertTrue(l.get_character("John") is c1)
        self.assertTrue(l.get_character("James") is c2)

    def test_mobs(self):
        l = Librarian()

        l.put_mob(Creature("Slime", hp=20))
        l.put_mob(Creature("cat", hp=10, attack_weight=1, defense_weight=2))
        l.put_mob(Creature("dog", hp=20, attack_damage=2))

        self.assertEquals(len(l.mob_names()), 3)

    def test_mob_cloning(self):

        l = Librarian()

        slime = Creature("Slime", hp=20)
        l.put_mob(slime)
        slime2 = l.get_mob("Slime")

        self.assertFalse(slime is slime2)


    def test_load_save(self):
        l = Librarian()
        c1 = Character("John")
        c2 = Character("James")
        l.put_character(c1)
        l.put_character(c2)
        
        self.assertTrue(l.get_character("John") is not None)
        self.assertTrue(l.get_character("James") is not None)

        self.assertTrue(l.get_character("John") is c1)
        self.assertTrue(l.get_character("James") is c2)

        l.save("test.dat")

        l2 = Librarian()
        l2.load("test.dat")

        self.assertTrue(len(l.character_names()), len(l2.character_names()))
        self.assertFalse(l.get_character("John") is l2.get_character("James"))

