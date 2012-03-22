from Battle.battle_side import BattleSide
from Battle.Attack.attack import Attack
from Battle.sideandaction import SideAndAction

import random

class Battle:
    """ Represents a Battle between two Trainers """
    
    def __init__(self, playerTrainer, oppTrainer):
        """ Builds the two participating sides of the battle """
        self.playerSide = BattleSide(playerTrainer)
        self.oppSide = BattleSide(oppTrainer)
        self.over = False
        
    def sendOutPkmnToStart(self):
        """ Sends out Pkmn on both sides """
        messages = []
        messages += self.oppSide.sendOutPkmnAtStart()
        messages += self.playerSide.sendOutPkmnAtStart()
        return messages
        
    def getActionsInOrder(self):
        """ Returns all the Actions for this turn in the Battle """
        oppAction = self.oppSide.trainer.getAction(self.getOppPkmn()[0], self.getPlayerPkmn())
        playerAction = self.playerSide.trainer.getAction(self.getPlayerPkmn()[0], self.getOppPkmn())
        
        actions = [oppAction] + [playerAction]
        actions.sort(reverse = True)
        return actions
                               
    def act(self, action):
        """ Performs the action """
        action.user.lastAction = action
        return action.doAction()
        
    def afterTurn(self, user):
        """ Perform affects of items/status/field hazards after the acting side performs its turn """
        return user.afterTurn()
        
    def betweenTurns(self):
        """ Perform between turns """
        self.playerSide.betweenTurns()
        self.oppSide.betweenTurns()
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