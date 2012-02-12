from Battle.Attack.EffectDelegates.heal_ratio_delegate import HealByRatioDelegate

class HealByHPRatioDelegate(HealByRatioDelegate):
    """ Represents an effect that heals """
        
    def heal(self, pkmn):
        """ Heals the target """
        total = pkmn.getStat("HP")
        toheal = total/self.healRatio
        pkmn.heal(toheal)