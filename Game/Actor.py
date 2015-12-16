class Actor(object):
    ''' Represent something which can act -- perhaps a character, perhaps a mob, perhaps...?'''
    def __init__(self, name, hp=100, attack_weight=0, attack_damage=0, defense_weight=0, defense_damage=0):
        self._items = []
        self._name = name
        self._attack_weight  = attack_weight
        self._attack_damage  = attack_damage
        self._defense_weight = defense_weight
        self._defense_damage = defense_damage
        self._base_hp = hp
        self._hp = hp

        self._exp = 0

    def name(self):
        ''' Name accessor '''
        return self._name

    def add_item(self, item):
        ''' Add an item to inventory '''
        self._items.append(item)

    def items():
        ''' get the inventory of items '''
        return self._items

    # TODO:  a) I'm repeating the same pattern over and overhere.  Do this introspectively to avoid repetition
    # TODO:  b) we need to abstract out a 'base' calculation, like with HP, so that it can grow with experience

    def attack_weight(self):
        ''' Calculate the value from a base and item buffs/debuffs '''
        return reduce(lambda x,y: x+y, [x._attack_weight for x in self._items], self._attack_weight)

    def attack_damage(self):
        ''' Calculate the value from a base and item buffs/debuffs '''
        return reduce(lambda x,y: x+y, [x._attack_damage for x in self._items], self._attack_damage)

    def defense_weight(self):
        ''' Calculate the value from a base and item buffs/debuffs '''
        return reduce(lambda x,y: x+y, [x._defense_weight for x in self._items], self._defense_weight)

    def defense_damage(self):
        ''' Calculate the value from a base and item buffs/debuffs '''
        return reduce(lambda x,y: x+y, [x._defense_damage for x in self._items], self._defense_damage)

    def hp(self):
        ''' Actor's actual current HP '''
        return self._hp

    def base_hp(self):
        ''' Actor's base HP when they're full healthy '''
        return self._base_hp

    def hurt(self, hp):
        ''' Hurt the actor -- deal this much damage '''
        self._hp -= hp

    def heal(self, hp):
        ''' Heal the actor '''
        self._hp += hp
        if self._hp > self.base_hp():
            self._hp = self.base_hp()

    def is_alive(self):
        ''' Check if we're alive '''
        return self._hp > 0

    def won(self):
        ''' Record that we won the fight.  Yay!'''
        self._exp += 1
    
