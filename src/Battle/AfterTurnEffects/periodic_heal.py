
class PeriodicHeal:
    """ Represents an effect that heals periodically after a turn """
    ratio = 16
    
    def __init__(self, message):
        """ Builds a Periodic Heal """
        self.message = message
        
    def afterTurn(self, side):
        """ Heals the given user """
        user = side.currPokemon
        self.heal(user)
        return [side.getHeader() + self.message]
        
    def heal(self, user):
        """ Heals the user """
        heal = self.getHeal(user)
        user.heal(heal)
        
    def getHeal(self, user):
        """ Returns the amount the pokemon should be healed by """
        return user.getRatioOfHealth(PeriodicHeal.ratio)