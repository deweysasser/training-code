class Item(object):
    ''' an item which has buff/debuff properties '''
    # TODO:  once again, I see the same pattern of argument lists and properties.  There should be some way to abstract this.  Mixin?
    def __init__(self, name, attack_weight=0, attack_damage=0, defense_weight=0, defense_damage=0, weight=1):
        self.name = name
        self._attack_weight  = attack_weight
        self._attack_damage  = attack_damage
        self._defense_weight = defense_weight
        self._defense_damage = defense_damage
        self._weight = weight

