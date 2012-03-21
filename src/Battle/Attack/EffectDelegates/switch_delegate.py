from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class SwitchDelegate(EffectDelegate):
    """ An Effect that switches the Pkmn with another Pkmn """
    
    def __init__(self, affectUser, reset):
        """ Builds a Switch Delegate """
        self.affectUser = affectUser
        self.reset = reset
    
    def applyEffect(self, user, target):
        """ Switches the user with another Pkmn on the side """
        pkmnWrapper = self.getEffectedPokemon(user, target)
        pkmn = self.getReplacement(pkmnWrapper)
        return pkmnWrapper.sendOutPkmn(pkmn, reset = self.reset)
        
    def getReplacement(self, pkmn):
        """ Returns the Pkmn to switch to """
        return pkmn.side.trainer.choosePokemon()