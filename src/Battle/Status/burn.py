from Battle.Status.status import Status

class Burn(Status):
    """ Represents a burn status """
    abbr = "BRN"
    start = " was burned."
    intermittent = " is hurt by its burn."
    done = " is no longer burned."
    ratio = 8
    
    def __init__(self):
        self.abbr = Burn.abbr
        self.setStatMods()
        self.statMods["ATK"] = .5
        
    def afterTurn(self, side):
        """ Perform affects of items/status/field hazards after the acting side performs its turn """
        user = side.currPokemon
        message = side.getHeader() + Burn.intermittent
        user.takeDamage(user.getRatioOfHealth(Burn.ratio))
        return [message]
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types is immune to the status """
        return "FIRE" in targetTypes