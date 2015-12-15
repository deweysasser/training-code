from Actor import *

class Creature(Actor):
    def __init__(self, name):
        super(Creature, self).__init__()
        self._name = name
