# the combat class
import random

class Combat(object):
    def __init__(self, actor1, actor2, seed=None):
        self.actors=[actor1, actor2]
        self.history = []
        if seed is None:
            self.random = random.Random()
        else:
            self.random = random.Random(seed)

    def fight(self):
        ''' Have the 2 actors fight, returning a history set '''
        while self.are_alive():
            self.history.append(self.exchange())

    def are_alive(self):
        return reduce(lambda x, y: x and y, [x.is_alive() for x in self.actors])

    def exchange(self):
        damage = 0
        if self.isHit(*self.actors):
            damage = self.damage(*self.actors)
            self.actors[1].hurt(damage)
        self.actors = list(reversed(self.actors))
        return ( damage, self.actors[1], self.actors[0])
        
    def isHit(self, a1, a2):
        return a1.attack_weight() + self.random.randrange(-5, 5) > a2.defense_weight()

    def damage(self, a1, a2):
        amount = a1.attack_damage() - a2.defense_damage() + self.random.randrange(0,10)
        if amount < 0: 
            return 0
        return amount
        
