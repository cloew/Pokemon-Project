from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class SwitchDelegate(EffectDelegate):
    """ An Effect that switches the Pkmn with another Pkmn """
    
    def __init__(self, reset):
        """ Builds a Switch Delegate """
        self.reset = reset
    
    def applyEffect(self, user, target):
        """ Switches the user with another Pkmn on the side """
        pkmn = user.side.trainer.choosePokemon()
        return user.sendOutPkmn(pkmn, reset = self.reset)