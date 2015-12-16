import pickle
import copy
import random

class Library(object):
    ''' Manage in-game characters, mobs, objects '''
    def __init__(self, seed=None):
        self._characters = {}
        self._mobs = {}
        self.items = {}
        self.random = random.Random(seed)

    def load(self, file):
        ''' Load library state from file'''
        with open(file) as f:
            self._characters = pickle.load(f)
            self._mobs = pickle.load(f)
            self.items = pickle.load(f)

        self.purge_dead()


    def save(self, file):
        ''' Save library state to file '''
        with open(file, "w") as f:
            pickle.dump(self._characters, f)
            pickle.dump(self._mobs, f)
            pickle.dump(self.items, f)

    def character_names(self):
        ''' return a list of character names '''
        return self._characters.keys()

    def mob_names(self):
        ''' return a list of mob names'''
        return self._mobs.keys()

    def items(self):
        ''' return the actual list of items '''
        return self.items

    def put_character(self, char):
        ''' Put the character into the library.  This will replace any existing chararacter of the same name.  Characters will be fully healed'''
        char.full_heal()
        self._characters[char.name()] = char

    def get_character(self, name):
        ''' get a character out of the library'''
        return self._characters[name]

    def purge_dead(self):
        ''' Purge dead characters from the library'''
        for k, v in copy.copy(self._characters).iteritems():
            if not v.is_alive():
                del self._characters[k]

    def put_mob(self, mob):
        ''' Put a mob into the library.  Replaces existing mob by name'''
        self._mobs[mob.name()] = mob

    def get_mob(self, name):
        ''' Get a copy of mob from library.  This clones a mob and doesn't affect the one already in the library'''
        return copy.deepcopy(self._mobs[name])

    def random_mob(self):
        ''' Get a random mob from the library.  Hero beware '''
        # a bit ugly -- perhaps we should not be naming mobs?
        names = self.mob_names()
        i = self.random.randrange(0, len(names))
        return self._mobs[names[i]]
    
            
