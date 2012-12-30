from Battle.Attack.EffectDelegates.charge_delegate import ChargeDelegate
from Battle.dodge import Dodge

class DodgeDelegate(ChargeDelegate):
    """ Represents an attack that dodges one turn and then attacks the next """
    
    def __init__(self, dodgeType, message):
        """ Builds a DodgeDelegate """
        self.turns = 2
        self.turnToAttack = 1
        self.message = message
        
        self.turnOn = 0
        self.dodgeType = dodgeType
    
    def applyEffect(self, user, target, environment):
        """ Applies the delegate's effect when the attack hits """
        return []
        
    def stopCharge(self, user):
        """ Stop Charging """
        user.dodge = None
        return super(DodgeDelegate, self).stopCharge(user)
    
    def isCharging(self, user):
        """ States when the attack is in the charging state """
        user.dodge = self.dodgeType
        return super(DodgeDelegate, self).isCharging(user)