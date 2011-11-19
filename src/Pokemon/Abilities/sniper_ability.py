from ability import Ability

class SniperAbility(Ability):
    """ An ability that triples damage on crit """
    
    def __init__(self, name):
        """ Builds the Ability """
        self.name = name
        
    def giveCrit(self, critMod):
        """ Triple crit damage """
        return 3