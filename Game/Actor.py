class Actor(object):
    def __init__(self):
        self._items = []
        self._attack_weight  = 0
        self._attack_damage  = 0
        self._defense_weight = 0
        self._defense_damage = 0

    def add_item(self, item):
        self._items.append(item)

    def attack_weight(self):
        return reduce(lambda x,y: x+y, [x._attack_weight for x in self._items], self._attack_weight)


    
