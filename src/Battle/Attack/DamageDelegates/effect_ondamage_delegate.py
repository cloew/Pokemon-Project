from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class EffectOnDamageDelegate(DamageDelegate):
    """ Does damage equivalent to half the target's current health """
    
    def takeDamage(self, damage, target):
        """ Has the target take damage """
        effects = self.parent.effectDelegates
        for effect in effects:
            if hasattr(effect, "setDamage"):
                effect.setDamage(damage)
                
        return super(EffectOnDamageDelegate, self).takeDamage(damage, target)