
class Leech():
    """ Represents a move that damages the pkmn applied to, and heals a source """
    ratio = 16
    
    def __init__(self, source, message):
        """ Build a Leech effect """
        self.source = source
        self.message = message
        
    def afterTurn(self, pkmn):
        """ Leech health from the pkmn and give it to the source """
        messages = [pkmn.getHeader() + self.message]
        
        messages += self.damage(pkmn)
        self.heal(pkmn)
        return messages
        
    def damage(self, pkmn):
        """ Damages the pkmn """
        return pkmn.takeDamage(self.getAmount(pkmn))

    def heal(self, pkmn):
        """ Heals the source """
        heal = self.getAmount(pkmn)
        self.source.heal(heal)
        
    def getAmount(self, pkmn):
        """ Returns the amount the Leech damages/heals """
        return pkmn.getRatioOfHealth(Leech.ratio)
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types are immune to the status """
        return "GRASS" in targetTypes
        