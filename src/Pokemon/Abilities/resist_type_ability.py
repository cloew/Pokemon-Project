from Pokemon.Abilities.ability import Ability

class ResistTypeAbility(Ability):
    """ An Ability with modified effectivensses """
    
    def __init__(self, name, types):
        """  """
        Ability.__init__(self, name)
        self.types = types
                        
    def effectivenessOnDefense(self, attackType, target):
        """ Returns the effectiveness of the attack when the Pokemon with this ability is defending """
        if attackType in self.types:
            return self.types[attackType]['effectiveness'], self.types[attackType]['message'].format(header=target.getHeader())
        return 1, None 