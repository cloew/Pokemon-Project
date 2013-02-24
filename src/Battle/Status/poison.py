from Battle.Status.status import Status

class Poison(Status):
    """ Represents a poison status """
    abbr = "PSN"
    start = " was poisoned."
    intermittent = " was hurt by poison."
    done = " is no longer poisoned."
    ratio = 8
    
    def __init__(self):
        self.initialize()
        
    def afterTurn(self, owner):
        """ Inflicts the damage from the Poison status """
        message = owner.getHeader() + Poison.intermittent
        owner.takeDamage(owner.getRatioOfHealth(Poison.ratio))
        return [message]
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types are immune to the status """
        return "POISON" in targetTypes or "STEEL" in targetTypes