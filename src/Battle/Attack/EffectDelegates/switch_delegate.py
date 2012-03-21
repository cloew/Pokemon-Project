from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class SwitchDelegate(EffectDelegate):
    """ An Effect that switches the Pkmn with another Pkmn """
    
    def applyEffect(self, user, target):
        """ Switches the user with another Pkmn on the side """
        pkmn = user.side.trainer.choosePokemon()
        return user.sendOutPkmn(pkmn, reset = False)