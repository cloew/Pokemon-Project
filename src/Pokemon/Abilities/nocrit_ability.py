from ability import Ability

class NoCritAbility(Ability):
    """ An ability that prevents any crit """
    
    def __init__(self, name):
        """ Builds the Ability """
        self.name = name
        
    def onCrit(self, critMod):
        """ Prevent the crit """
        return 1