from Battle.Attack.EffectDelegates.heal_ratio_delegate import HealByRatioDelegate

class HealByHPRatioDelegate(HealByRatioDelegate):
    """ Represents an effect that heals """
        
    def heal(self, side):
        """ Heals the target """
        target = side.currPokemon
        total = target.battleDelegate.stats["HP"]
        toheal = total/self.healRatio
        target.battleDelegate.heal(toheal)