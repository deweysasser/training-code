from Actor import *

class Character(Actor):
    def __init__(self, name, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)
        self._name = name

    def full_heal(self):
        self._hp = self._base_hp
