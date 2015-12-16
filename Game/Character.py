from Actor import *
import math

class Character(Actor):
    ''' An actor representing a game player '''
    def __init__(self, name, *args, **kwargs):
        super(Character, self).__init__(name, *args, **kwargs)

    def full_heal(self):
        ''' Restore HP to base HP '''
        # TODO: there's a bug here -- this should use the base_hp()
        # method.  Clearly I've never tested this case despite the
        # fact that we've covered it
        self._hp = self._base_

    def base_hp(self):
        ''' Character base HP is based on actual base HP plus a factor related to experience '''
        if self._exp < 1:
            return super(Character, self).base_hp()
        else:
            return super(Character, self).base_hp() + int(20*math.log(self._exp, 10))
