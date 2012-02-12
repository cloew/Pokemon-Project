from Battle.Attack.EffectDelegates.heal_ratio_delegate import HealByRatioDelegate

class HealByDamageRatioDelegate(HealByRatioDelegate):
    """ Represents an effect that heals """
        
    def setDamage(self, damage):
        """ Sets the total to heal a ratio of """
        self.damage = damage
        
    def heal(self, pkmn):
        """ Heals the target """
        toheal = self.damage/self.healRatio
        pkmn.heal(toheal)