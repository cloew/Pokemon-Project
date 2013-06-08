from Pokemon.Abilities.ability import Ability


class SkipTurnAbility(Ability): 
    """ An ability that cause the Pkmn to only attack every other turn """
    message = " is loafing around."
    
    def __init__(self, name):
        """  """
        super(SkipTurnAbility, self).__init__(name)
        self.stop = 1
        
    def stopAttack(self, pkmn):
        """ Return whether the Pkmn should not be able to attack """
        messages = []
        self.toggleStop()
        
        if self.stop:
            messages.append(pkmn.getHeader() + self.message)
            
        return self.stop, messages
        
    def onCharge(self):
        """ On charge, toggle the stop setting """
        self.toggleStop()
        
    def toggleStop(self):
        """ Toggles the Stop setting of the Ability """
        self.stop = not self.stop