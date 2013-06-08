from ability import Ability

class ConfusionImmunityAbility(Ability):
    """ Represents an ability that makes the owner immune to confusion """
    
    def __init__(self, name):
        """ Builds the Confuse """
        Ability.__init__(self, name)
    
    def canBeConfused(self, pkmn, messages):
        """ Return if the pokemon can be confused """
        message = "{0}'s {1} prevented confusion.".format(pkmn.getName(), self.name)
        messages.append(message)
        return False 