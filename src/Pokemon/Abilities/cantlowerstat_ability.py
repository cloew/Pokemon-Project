from ability import Ability

class CantLowerStatAbility(Ability):
    """ An ability that prevents the opp from lowering a stat """
    message = "%s's %s prevented it's %s from being lowered."
    
    def __init__(self, name, stat):
        """ Builds the Ability """
        super(CantLowerStatAbility, self).__init__(name)
        self.stat = stat
        
    def onStatMod(self, pkmn, stat, degree, selfInflicted):
        """ Alter the statMods of the Status to reflect the abilities effect """
        messages = []
        
        if not selfInflicted and stat == self.stat and degree < 0:
            degree = 0
            messages = [self.message % (pkmn.getHeader(), self.name, self.stat)]
            
        return degree, messages