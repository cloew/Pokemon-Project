from ability import Ability

class SniperAbility(Ability):
    """ An ability that triples damage on crit """
    
    def __init__(self, name):
        """ Builds the Ability """
        super(SniperAbility, self).__init__()
        self.name = name
        
    def giveCrit(self, critMod):
        """ Triple crit damage """
        return 3