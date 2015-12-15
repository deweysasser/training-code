import pickle
import copy
import random

class Librarian(object):
    ''' Manage in-game characters, mobs, objects '''
    def __init__(self, seed=None):
        self.characters = {}
        self.mobs = []
        self.items = []
        self.random = random.Random(seed)

    def load(self, file):
        with open(file) as f:
            self.characters = pickle.load(f)
            self.mobs = pickle.load(f)
            self.items = pickle.load(f)

    def save(self, file):
        with open(file, "w") as f:
            pickle.dump(self.characters, f)
            pickle.dump(self.mobs, f)
            pickle.dump(self.items, f)

    def character_names(self):
        return self.characters.keys()

    def mob_names(self):
        return [x._name for x in self.mobs]

    def items(self):
        return self.items

    def character(self, name, ch=None):
        if ch is not None:
            ch.full_heal()
            self.characters[name] = ch

        return self.characters[name]

    def purge(self):
        for k, v in self.characters:
            if not v.is_alive():
                del self.characters[k]

    def mob(self, name, mo=None):
        if mo is not None:
            self.mobs[name] = mo
        return copy.deepcopy(self.mobs[name])

    def random_mob(self):
        # a bit ugly -- perhaps we should not be naming mobs?
        names = self.mob_names()
        i = self.random.randrange(0, names)
        return self.mob(names[i])
    
            
