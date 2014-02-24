from Battle.Attack.Steps.attack_step import AttackStep

class RemovePPStep(AttackStep):
    """ Represents the Remove PP Step in the Attack Process """
    
    def perform(self, user, target, environment):
        """ Perform this step """
        if self.parent.currPowerPoints > 0:
            self.parent.currPowerPoints -= 1
        return []