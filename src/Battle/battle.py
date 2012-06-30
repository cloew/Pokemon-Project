from Battle.battle_side import BattleSide
from Battle.Attack.attack import Attack
from Battle.battle_round import BattleRound

import random

class Battle:
    """ Represents a Battle between two Trainers """
    
    def __init__(self, playerTrainer, oppTrainer):
        """ Builds the two participating sides of the battle """
        self.playerSide = BattleSide(playerTrainer)
        self.oppSide = BattleSide(oppTrainer)
        self.over = False
        self.round = BattleRound(self.playerSide, self.oppSide)
        
    def sendOutPkmnToStart(self):
        """ Sends out Pkmn on both sides """
        messages = []
        messages += self.oppSide.sendOutPkmnAtStart()
        messages += self.playerSide.sendOutPkmnAtStart()
        return messages
        
    def select(self):
        """ Handles a select command based on the state of the battle
             ... very very icky... """
        if len(self.messageQueue) > 0:
            if self.messageQueue[0].fullyDisplayed:
                self.messageQueue.popleft()
        
    def performRound(self):
        """  Performs a single round """
        self.round.run()
        self.betweenRounds()
        return self.round.messageQueue
        
    def betweenRounds(self):
        """ Perform between rounds """
        self.playerSide.betweenRounds()
        self.oppSide.betweenRounds()
        return []
        
    def refillSides(self):
        """ Refills fainted Pkmn on each side """
        messages =  self.checkOver()
        if self.over:
            return messages
            
        messages += self.playerSide.refill()
        messages += self.oppSide.refill()
        return messages
        
    def checkOver(self):
        """ Checks if the game is Over """
        messages = self.checkOverForSide(self.playerSide)
        if self.over:
            return messages
            
        messages = self.checkOverForSide(self.oppSide)
        return messages
        
    def checkOverForSide(self, side):
        """ Checks if the game is over because the side has no Pkmn """
        messages = []
        
        if not side.hasPokemon():
            self.over = True
            messages.append(side.trainer.beaten())
        return messages
        
    def getPlayerTrainer(self):
        """ Returns the Playing Trainer """
        return self.playerSide.trainer
    
    def getOppTrainer(self):
        """ Returns the Opposing Trainer """
        return self.oppSide.trainer
        
    def getPlayerPkmn(self):
        """ Returns the Pokemon currently out """
        return self.playerSide.pkmnInPlay
        
    def getOppPkmn(self):
        """ Returns the Pokemon currently out """
        return self.oppSide.pkmnInPlay