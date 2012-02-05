from secondary_effect import SecondaryEffect

class PeriodicHeal(SecondaryEffect):
    """ Represents an effect that heals periodically after a turn """
    ratio = 16
    
    def __init__(self, message):
        """ Builds a Periodic Heal """
        self.message = message
        
    def afterTurn(self, user):
        """ Heals the given user (User is a pkmnBattleWrapper) """
        self.heal(user.pkmn)
        return [user.getHeader() + self.message]
        
    def heal(self, pkmn):
        """ Heals the given Pokemon """
        heal = self.getHeal(pkmn)
        pkmn.heal(heal)
        
    def getHeal(self, pkmn):
        """ Returns the amount the pokemon should be healed by """
        return pkmn.getRatioOfHealth(PeriodicHeal.ratio)