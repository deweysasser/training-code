import unittest
from Librarian import *
from Character import *

class testLibrarian(unittest.TestCase):
    def test_characters(self):
        l = Librarian()
        c1 = Character("John")
        c2 = Character("James")
        l.character("John", c1)
        l.character("James", c2)
        
        self.assertTrue(l.character("John") is not None)
        self.assertTrue(l.character("James") is not None)

        self.assertTrue(l.character("John") is c1)
        self.assertTrue(l.character("James") is c2)



    def test_load_save(self):
        l = Librarian()
        c1 = Character("John")
        c2 = Character("James")
        l.character("John", c1)
        l.character("James", c2)
        
        self.assertTrue(l.character("John") is not None)
        self.assertTrue(l.character("James") is not None)

        self.assertTrue(l.character("John") is c1)
        self.assertTrue(l.character("James") is c2)

        l.save("test.dat")

        l2 = Librarian()
        l2.load("test.dat")

        self.assertTrue(len(l.character_names()), len(l2.character_names()))
        self.assertFalse(l.character("John") is l2.character("James"))
