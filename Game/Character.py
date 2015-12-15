from Actor import *
import math

class Character(Actor):
    def __init__(self, name, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)
        self._name = name

    def full_heal(self):
        self._hp = self._base_hp


    def base_hp(self):
        if self._exp < 1:
            return super(Character, self).base_hp()
        else:
            return super(Character, self).base_hp() + int(20*math.log(self._exp, 10))
