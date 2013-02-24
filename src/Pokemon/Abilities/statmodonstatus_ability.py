from ability import Ability

class StatModOnStatusAbility(Ability):
    """ An ability that modifies a stat when the parent receives a status """
    
    def __init__(self, name, stat, mod):
        """ Builds the Ability """
        super(StatModOnStatusAbility, self).__init__()
        self.name = name
        self.stat = stat
        self.mod = mod
        
    def onStatus(self, pkmn, status):
        """ Alter the statMods of the Status to reflect the abilities effect """
        messages = []
        
        status.statMods[self.stat] = self.mod
        messages = [pkmn.getHeader() + " raised it's " + self.stat + "."]
            
        return messages