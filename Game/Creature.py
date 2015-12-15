from Actor import *

class Creature(Actor):
    def __init__(self, name, *args, **kwargs):
        super(Creature, self).__init__(name, *args, **kwargs)
