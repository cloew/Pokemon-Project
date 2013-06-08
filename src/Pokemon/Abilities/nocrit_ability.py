from ability import Ability

class NoCritAbility(Ability):
    """ An ability that prevents any crit """
        
    def takeCrit(self, critMod, thisSide, otherSide):
        """ Prevent the crit """
        return 1, []