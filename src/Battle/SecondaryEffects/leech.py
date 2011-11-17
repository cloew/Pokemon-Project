from secondary_effect import SecondaryEffect

class Leech(SecondaryEffect):
    """ Represents a move that damages the side applied to, and heals a source """
    ratio = 16
    
    def __init__(self, source, message):
        """ Build a Leech effect """
        self.source = source
        self.message = message
        
    def afterTurn(self, side):
        """ Leech health from the user and give it to the source """
        user = side.currPokemon
        self.damage(user)
        self.heal(user)
        return [side.getHeader() + self.message]
        
    def damage(self, user):
        """ Damages the user """
        user.takeDamage(self.getAmount(user))

    def heal(self, user):
        """ Heals the source """
        heal = self.getAmount(user)
        self.source.heal(heal)
        
    def getAmount(self, user):
        """ Returns the amount the Leech damages/heals """
        return user.getRatioOfHealth(Leech.ratio)
        
    def immune(self, targetTypes, attackType):
        """ Returns whether the given types are immune to the status """
        return "GRASS" in targetTypes
        