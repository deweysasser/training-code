class Actor(object):
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
        return self._name

    def add_item(self, item):
        self._items.append(item)

    def items():
        return self._items

    def attack_weight(self):
        return reduce(lambda x,y: x+y, [x._attack_weight for x in self._items], self._attack_weight)

    def attack_damage(self):
        return reduce(lambda x,y: x+y, [x._attack_damage for x in self._items], self._attack_damage)

    def defense_weight(self):
        return reduce(lambda x,y: x+y, [x._defense_weight for x in self._items], self._defense_weight)

    def defense_damage(self):
        return reduce(lambda x,y: x+y, [x._defense_damage for x in self._items], self._defense_damage)

    def hp(self):
        return self._hp

    def base_hp(self):
        return self._base_hp

    def hurt(self, hp):
        self._hp -= hp

    def heal(self, hp):
        self._hp += hp
        if self._hp > self.base_hp():
            self._hp = self.base_hp()

    def is_alive(self):
        return self._hp > 0

    def won(self):
        self._exp += 1
    
