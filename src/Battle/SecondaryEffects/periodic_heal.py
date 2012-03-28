from secondary_effect import SecondaryEffect
from Battle.FaintHandlers.faint_handler_factory import FaintHandlerFactory

class PeriodicHeal(SecondaryEffect):
    """ Represents an effect that heals periodically after a turn """
    ratio = 16
    
    def __init__(self, message):
        """ Builds a Periodic Heal """
        self.message = message
        self.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.USER)
        
    def afterTurn(self, owner):
        """ Heals the given owner"""
        self.heal(owner)
        return [owner.getHeader() + self.message]
        
    def heal(self, owner):
        """ Heals the given Pokemon """
        heal = self.getHeal(owner)
        owner.heal(heal)
        
    def getHeal(self, owner):
        """ Returns the amount the pokemon should be healed by """
        return owner.getRatioOfHealth(PeriodicHeal.ratio)