from Battle.Attack.Steps.attack_step import AttackStep

class DamageStep(AttackStep):
    """ Represents the Damage Step in the Attack Process """
    
    def perform(self, user, target, environment):
        """ Perform this step """
        return self.parent.damageDelegate.doDamage(user, target, environment)