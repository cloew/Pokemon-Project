from Battle.Status.status import Status

class Poison(Status):
    """ Represents a poison status """
    abbr = "PSN"
    start = " was poisoned."
    intermittent = " was hurt by poison."
    done = " is no longer poisoned."
    ratio = 8
    
    def __init__(self):
        self.abbr = Poison.abbr
        self.setStatMods()
        
    def afterTurn(self, side):
        """ Inflicts the damage from the Poison status """
        user = side.currPokemon
        message = side.getHeader() + Poison.intermittent
        user.takeDamage(user.getRatioOfHealth(Poison.ratio))
        return [message]
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types are immune to the status """
        return "POISON" in targetTypes or "STEEL" in targetTypes