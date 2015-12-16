import unittest
from Library import *
from Character import *
from Creature import *

class testLibrary(unittest.TestCase):
    def test_characters(self):
        l = Library()
        c1 = Character("John")
        c2 = Character("James")
        l.put_character(c1)
        l.put_character(c2)

        self.assertTrue(l.get_character("John") is not None)
        self.assertTrue(l.get_character("James") is not None)

        self.assertTrue(l.get_character("John") is c1)
        self.assertTrue(l.get_character("James") is c2)

    def test_mobs(self):
        l = Library()

        l.put_mob(Creature("Slime", hp=20))
        l.put_mob(Creature("cat", hp=10, attack_weight=1, defense_weight=2))
        l.put_mob(Creature("dog", hp=20, attack_damage=2))

        self.assertEquals(len(l.mob_names()), 3)

    def test_mob_cloning(self):

        l = Library()

        slime = Creature("Slime", hp=20)
        l.put_mob(slime)
        slime2 = l.get_mob("Slime")

        self.assertFalse(slime is slime2)


    def test_load_save(self):
        l = Library()
        c1 = Character("John")
        c2 = Character("James")
        l.put_character(c1)
        l.put_character(c2)
        
        self.assertTrue(l.get_character("John") is not None)
        self.assertTrue(l.get_character("James") is not None)

        self.assertTrue(l.get_character("John") is c1)
        self.assertTrue(l.get_character("James") is c2)

        l.save("test.dat")

        l2 = Library()
        l2.load("test.dat")

        self.assertTrue(len(l.character_names()), len(l2.character_names()))
        self.assertFalse(l.get_character("John") is l2.get_character("James"))



    def test_purge(self):
        l = Library()
        c1 = Character("John")
        l.put_character(c1)


        self.assertEquals(len(l.character_names()), 1)

        c1.hurt(c1.hp() + 1)

        l.purge_dead()

        self.assertEquals(len(l.character_names()), 0)

    def test_random_mob(self):
        l = Library(seed=0)

        l.put_mob(Creature("Slime", hp=20))
        l.put_mob(Creature("cat", hp=10, attack_weight=1, defense_weight=2))
        l.put_mob(Creature("dog", hp=20, attack_damage=2))

        self.assertEquals(l.random_mob().name(), "cat")
        
        
