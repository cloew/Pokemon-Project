from Battle.Attack.EffectDelegates.switch_delegate import SwitchDelegate

class RandomSwitchDelegate(SwitchDelegate):
    """ An Effect that switches the Pkmn with another Pkmn """
    
    def getReplacement(self, pkmn):
        """ Returns the Pkmn to switch to  """
        return pkmn.side.trainer.chooseRandomPokemon(pkmn.side.pkmnInPlay)