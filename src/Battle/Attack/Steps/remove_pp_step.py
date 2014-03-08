from Battle.Attack.Steps.attack_step import AttackStep
from Battle.Attack.HitDelegates.hitself_delegate import HitSelfDelegate

class RemovePPStep(AttackStep):
    """ Represents the Remove PP Step in the Attack Process """
    
    def perform(self, user, target, environment):
        """ Perform this step """
        pressure = self.getPressure(target)
        
        if self.parent.currPowerPoints > 0:
            self.parent.currPowerPoints -= pressure
        return []
        
    def getPressure(self, target):
        """ Return the Pressure exerted when using the attack """
        if isinstance(self.parent.hitDelegate, HitSelfDelegate):
            return 1
        else:
            return target.getAbility().powerPointsPressure()