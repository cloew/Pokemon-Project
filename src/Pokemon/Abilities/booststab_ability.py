from ability import Ability

class BoostStabAbility(Ability):
    """ An ability that boosts the mod of STAB """
    stabMod = 2
    
    def __init__(self, name):
        """ Builds the Ability """
        super(BoostStabAbility, self).__init__()
        self.name = name