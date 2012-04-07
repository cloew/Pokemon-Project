import random
from Battle.Attack.EffectDelegates.multi_turn_delegate import MultiTurnDelegate

class MultiTurnRangeDelegate(MultiTurnDelegate):
    """ An Effect that forces the same attack to be used for a variable number of turns """
    
    def __init__(self, min, max, effects):
        """ Builds a Multi Turn Effect that will perform the given effects when it ends """
        self.min = min
        self.max = max
        
        MultiTurnDelegate.__init__(self, effects)
        
    def resetTurns(self):
        """ Reset the Turns left for the effect """
        self.getTurns()
        MultiTurnDelegate.resetTurns(self)
    
    def getTurns(self):
        """ Gets the number of turns this attack will last """
        self.turns = random.randint(self.min, self.max)