from Battle.Actions.action_lock import ActionLock
from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class DamageScaleDelegate(DamageDelegate):
    
    def __init__(self, parent, power, isPhysical, factor, turns):
        """ """
        self.parent = parent
        self.power = power
        self.isPhysical = isPhysical
        self.factor = factor
        self.turns = turns
        
        self.turnOn = 0
        
    def coreDamage(self, actingSide, otherSide):
        """ Calculate the damage before modifiers and rands """
        user = actingSide.currPokemon
        target = otherSide.currPokemon
        
        atkStat, defStat = self.getAtkAndDefType()
    
        attack = self.getStatWithMod(atkStat, actingSide)
        defense = self.getStatWithMod(defStat, otherSide)
        level = user.level
        scale = self.getScale()
        
        return ((((2*level/5 + 2)*attack*self.power*scale/defense)/50) + 2)
        
    def getScale(self):
        """ Returns the scale based on the number of turns the attack has run """
        return self.factor**self.turnOn
        
    def applyEffect(self, actingSide, otherSide):
        """ Applies the delegate's effect when the attack hits """
        if self.turnOn == 0:
            self.applyLock(actingSide)
            
        self.incTurns()
        return []
        
    def effectOnMiss(self, actingSide, otherSide):
        """ Applies the deleagte's effect on a miss """
        self.turnOn = 0
        actingSide.trainer.actionLock = None
        return []
        
    def incTurns(self):
        """ Move to the next turn """
        self.turnOn = (self.turnOn+1)%self.turns
        
    def applyLock(self, side):
        """ Locks the side to use this move """
        side.trainer.actionLock = ActionLock(side.trainer,  \
                                                        side.lastAction, self.turns-1)