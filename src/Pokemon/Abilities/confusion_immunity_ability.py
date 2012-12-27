from ability import Ability

class ConfusionImmunityAbility(Ability):
    """ Represents an ability that makes the owner immune to confusion """
    
    def __init__(self, name):
        """ Builds the Confuse """
        self.name = name
    
    def canBeConfused(self, messages):
        """ Return if the pokemon can be confused """
        message = "{0} prevented confusion.".format(self.name)
        messages.append(message)
        return False 