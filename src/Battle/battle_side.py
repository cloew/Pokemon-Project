from Battle.pkmn_battle_wrapper import PkmnBattleWrapper
from Trainer.trainer import Trainer

class BattleSide:
    """ Holds the data for a side of a battle """
    
    def __init__(self, trainer):
        """  """
        self.trainer = trainer
        self.pkmnInPlay = [PkmnBattleWrapper(self)]
        
    def sendOutPkmn(self):
        """  Send out Pokemon to fill out all pkmnInPlay """
        messages = []
        
        for i in range(0, len(self.pkmnInPlay)):
            pkmn = self.trainer.getPokemon(i)
            if not pkmn:
                break
            
            messages.append(self.pkmnInPlay[i].sendOutPkmn(pkmn))
            
        return messages
        
    def hasMorePokemon(self):
        """ Returns whether this side has more Pokemon """
        return self.trainer.hasMorePokemon()
        
    def betweenTurns(self):
        """ Perform between turns """
        for pkmn in self.pkmnInPlay:
            pkmn.betweenTurns()