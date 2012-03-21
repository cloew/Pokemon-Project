from Battle.Attack.EffectDelegates.switch_delegate import SwitchDelegate

class RandomSwitchDelegate(SwitchDelegate):
    """ An Effect that switches the Pkmn with another Pkmn """
    
    def __init__(self, reset):
        """ Builds a Switch Delegate """
        self.reset = reset
    
    def getReplacement(self, pkmn):
        """ Returns the Pkmn to switch to  """
        return pkmn.side.trainer.chooseRandomPokemon(pkmn.pkmn)