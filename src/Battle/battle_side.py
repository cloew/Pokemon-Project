from Battle.pkmn_battle_wrapper import PkmnBattleWrapper
from Trainer.trainer import Trainer

class BattleSide:
    """ Holds the data for a side of a battle """
    
    def __init__(self, trainer):
        """  """
        self.trainer = trainer
        self.pkmnInPlay = [PkmnBattleWrapper(self)]
        
    def sendOutPkmnAtStart(self):
        """ Send out Pokemon to fill out all pkmnInPlay at the start of a battle """
        messages = []
        
        for i in range(0, len(self.pkmnInPlay)):
            pkmn = self.trainer.getPokemon(i)
            if not pkmn:
                break
            messages += self.pkmnInPlay[i].sendOutPkmn(pkmn)
        
        return messages
        
    def sendOutPkmn(self, pokemonToReplace, pokemonReplacements):
        """ Send out a Pokemon  """
        messages = []
        if pokemonToReplace in pokemonReplacements:
            pkmn = pokemonReplacements[pokemonToReplace]
        else:
            pkmn = self.trainer.choosePokemon(self.pkmnInPlay)
        messages += pokemonToReplace.sendOutPkmn(pkmn)
        return messages
        
    def hasPokemon(self):
        """ Returns whether this side has more Pokemon """
        return self.trainer.hasPokemon()
        
    def hasMorePokemon(self):
        """ Returns whether this side has more Pokemon """
        return self.trainer.hasMorePokemon(self.pkmnInPlay)
        
    def betweenRounds(self):
        """ Perform between turns """
        for pkmn in self.pkmnInPlay:
            pkmn.betweenRounds()
            
    def refill(self, pokemonReplacements):
        """ Refills the Pkmn In Play """
        messages = []
        if not self.hasMorePokemon():
            return messages
            
        for pkmn in self.pkmnInPlay:
            if pkmn.fainted():
                messages += self.sendOutPkmn(pkmn, pokemonReplacements)
                
        return messages
        
    def awardExperience(self, pkmnToAwardExperienceFrom):
        """ Award experience to current pokemon from the opposing pokemon """
        messages = []
        
        for oppPkmn in pkmnToAwardExperienceFrom:
            experienceToAward = oppPkmn.experienceToAward
            for pkmn in self.pkmnInPlay:
                pkmn.gainExperience(experienceToAward)
                messages += ["{0} gained {1} experience points.".format(pkmn.name, experienceToAward)]
                while pkmn.canLevelUp():
                    messages += pkmn.levelUp()
                
        return messages
        
    def beaten(self):
        """ Returns the string saying the side was beaten """
        return [self.trainer.beaten()]