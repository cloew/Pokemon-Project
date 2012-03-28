from secondary_effect import SecondaryEffect

from Battle.FaintHandlers.faint_handler_factory import FaintHandlerFactory

class Leech(SecondaryEffect):
    """ Represents a move that damages the side applied to, and heals a source """
    ratio = 16
    
    def __init__(self, source, message):
        """ Build a Leech effect """
        self.source = source
        self.message = message
        self.faintHandler = FaintHandlerFactory.buildFromType(FaintHandlerFactory.SOURCE)
        
    def afterTurn(self, owner):
        """ Leech health from the owner and give it to the source """
        messages = [owner.getHeader() + self.message]
        
        messages += self.damage(owner)
        self.leech(owner)
        return messages
        
    def damage(self, owner):
        """ Damages the owner """
        return owner.takeDamage(self.getAmount(owner))

    def leech(self, owner):
        """ Leech Health from the owner and heal the source """
        heal = self.getAmount(owner)
        self.source.heal(heal)
        
    def getAmount(self, owner):
        """ Returns the amount the Leech damages/heals """
        return owner.getRatioOfHealth(Leech.ratio, forDamage = True)
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types are immune to the status """
        return "GRASS" in targetTypes
        