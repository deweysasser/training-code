from Actor import *

class Character(Actor):
    def __init__(self, name, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)
        self._name = name
        self._exp = 0
