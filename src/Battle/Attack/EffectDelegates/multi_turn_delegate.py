from Battle.Actions.action_lock import ActionLock
from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class MultiTurnDelegate(EffectDelegate):
    """ An Effect that forces the same attack to be used for some number of turns """
    
    def __init__(self, turns, effects):
        """ Builds a Multi Turn Effect that will perform the given effects when it ends """
        self.turns = turns
        self.turnOn = 0
        self.effects = effects
    
    def applyEffect(self, user, target):
        """ Lock Attack if this is the first time, Call Effects if lock is over """
        if self.turnOn == 0:
            self.applyLock(user)
        
        self.incTurns()
        return self.checkOver(user, target)
        
    def incTurns(self):
        """ Move to the next turn """
        self.turnOn = (self.turnOn+1)%self.turns
        
    def applyLock(self, pkmn):
        """ Locks the side to use this move """
        pkmn.actionLock = ActionLock(pkmn,  pkmn.lastAction, self.turns-1)
        
    def checkOver(self, user, target):
        """ Checks if the Lock is over, if so it performs the extra effects """
        messages = []
        over = (self.turnOn == 0)
        if over:
            messages += self.performEffects(self.effects, user, target)
        
        return messages