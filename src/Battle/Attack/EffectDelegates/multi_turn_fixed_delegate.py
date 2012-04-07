from Battle.Attack.EffectDelegates.multi_turn_delegate import MultiTurnDelegate

class FixedMultiTurnDelegate(MultiTurnDelegate):
    """ An Effect that forces the same attack to be used for some fixed number of turns """
    
    def __init__(self, turns, effects):
        """ Builds a Fixed Multi Turn Effect that will perform the given effects when it ends """
        self.turns = turns
        MultiTurnDelegate.__init__(self, effects)