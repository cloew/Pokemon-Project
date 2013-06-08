from ability import Ability

class SniperAbility(Ability):
    """ An ability that triples damage on crit """
        
    def giveCrit(self, critMod):
        """ Triple crit damage """
        return 3