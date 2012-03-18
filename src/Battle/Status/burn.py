from Battle.Status.status import Status

class Burn(Status):
    """ Represents a burn status """
    abbr = "BRN"
    start = " was burned."
    intermittent = " is hurt by its burn."
    done = " is no longer burned."
    ratio = 8
    
    def __init__(self):
        self.initialize()
        self.statMods["ATK"] = .5
        
    def afterTurn(self, pkmn):
        """ Perform affects of status after the Pkmn performs its turn """
        message = pkmn.getHeader() + Burn.intermittent
        pkmn.takeDamage(pkmn.getRatioOfHealth(Burn.ratio))
        return [message]
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types is immune to the status """
        return "FIRE" in targetTypes