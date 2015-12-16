from Actor import *

class Creature(Actor):
    ''' An actor that is a creature.  They're dumb -- no XP stats bonuses'''
    def __init__(self, name, *args, **kwargs):
        super(Creature, self).__init__(name, *args, **kwargs)
