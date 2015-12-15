import pickle
import copy
import random

class Librarian(object):
    ''' Manage in-game characters, mobs, objects '''
    def __init__(self, seed=None):
        self._characters = {}
        self._mobs = {}
        self.items = {}
        self.random = random.Random(seed)

    def load(self, file):
        with open(file) as f:
            self._characters = pickle.load(f)
            self._mobs = pickle.load(f)
            self.items = pickle.load(f)

    def save(self, file):
        with open(file, "w") as f:
            pickle.dump(self._characters, f)
            pickle.dump(self._mobs, f)
            pickle.dump(self.items, f)

    def character_names(self):
        return self._characters.keys()

    def mob_names(self):
        return self._mobs.keys()

    def items(self):
        return self.items

    def put_character(self, char):
        char.full_heal()
        self._characters[char.name()] = char

    def get_character(self, name):
        return self._characters[name]

    def purge_dead(self):
        for k, v in self._characters:
            if not v.is_alive():
                del self._characters[k]

    def put_mob(self, mob):
        self._mobs[mob.name()] = mob

    def get_mob(self, name):
        return copy.deepcopy(self._mobs[name])

    def random_mob(self):
        # a bit ugly -- perhaps we should not be naming mobs?
        names = self.mob_names()
        i = self.random.randrange(0, names)
        return self.mob(names[i])
    
            
