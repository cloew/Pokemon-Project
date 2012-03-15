from secondary_effect import SecondaryEffect

class Leech(SecondaryEffect):
    """ Represents a move that damages the side applied to, and heals a source """
    ratio = 16
    
    def __init__(self, source, message):
        """ Build a Leech effect """
        self.source = source
        self.message = message
        
    def afterTurn(self, pkmn):
        """ Leech health from the pkmn and give it to the source """
        messages = [pkmn.getHeader() + self.message]
        
        messages += self.damage(pkmn)
        self.leech(pkmn)
        return messages
        
    def damage(self, pkmn):
        """ Damages the pkmn """
        return pkmn.takeDamage(self.getAmount(pkmn))

    def leech(self, pkmn):
        """ Leech Health from the pkmn and heal the source """
        heal = self.getAmount(pkmn)
        self.source.heal(heal)
        
    def getAmount(self, pkmn):
        """ Returns the amount the Leech damages/heals """
        return pkmn.getRatioOfHealth(Leech.ratio, forDamage = True)
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types are immune to the status """
        return "GRASS" in targetTypes
        