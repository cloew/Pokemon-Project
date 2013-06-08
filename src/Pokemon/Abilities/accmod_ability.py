from ability import Ability

class AccModAbility(Ability):
    """ An ability that modifies the accuracy of moves"""
    
    def __init__(self, name, mod):
        """ Builds the Ability """
        super(AccModAbility, self).__init__(name)
        self.mod = mod
        
    def onAccuracy(self, accuracy):
        """ Modify the accuracy """
        return accuracy*self.mod