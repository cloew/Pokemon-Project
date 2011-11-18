from ability import Ability

class CantLowerStatAbility(Ability):
    """ An ability that prevents the opp from lowering a stat """
    message = "%s's %s prevented it's %s from being lowered."
    
    def __init__(self, name, stat):
        """ Builds the Ability """
        self.name = name
        self.stat = stat
        
    def onStatMod(self, side, stat, degree, affectUser):
        """ Alter the statMods of the Status to reflect the abilities effect """
        messages = []
        
        if not affectUser and stat == self.stat and degree < 0:
            degree = 0
            messages = [self.message % (side.getHeader(), self.name, self.stat)]
            
        return degree, messages