from Battle.Status.poison import Poison

class ToxicPoison(Poison):
    """ Represents a poison status """
    abbr = "BPSN"
    start = " was badly poisoned."
    ratio = 16
    
    def __init__(self):
        self.abbr = Poison.abbr
        self.counter = 1
        
        self.setStatMods()
        
    def afterTurn(self, pkmn):
        """ Inflicts the damage from the Poison status """
        user = pkmn.pkmn
        message = pkmn.getHeader() + Poison.intermittent
        damage = self.getDamage(user)
        
        user.takeDamage(damage)
        self.counter = self.counter + 1
        return [message]
        
    def getDamage(self, user):
        """ Returns the damage dealt by the toxic poison """
        ratio = user.getRatioOfHealth(ToxicPoison.ratio)
        return ratio*self.counter