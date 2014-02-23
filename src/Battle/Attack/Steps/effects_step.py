from Battle.Attack.Steps.attack_step import AttackStep

class EffectsStep(AttackStep):
    """ Represents the Effects Step in the Attack Process """
    
    def perform(self, user, target, environment):
        """ Perform this step """
        messages = []
        
        if not self.preventEffects(user, target):
            for effect in self.parent.effectDelegates:
                messages += effect.tryToApplyEffect(user, target, environment)
        return messages
    
        
    def preventEffects(self, user, target):
        """ Return whether the effects are prevented """
        nullDamage = hasattr(self.parent.damageDelegate, "isNull")
        canUse = user.getAbility().canUseEffects() and target.getAbility().canUseEffects()
        return not nullDamage and not canUse