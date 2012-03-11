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
        
    def afterTurn(self, user, target, func):
        """ Perform affects of items/status/field hazards after the acting side performs its turn """
        return user.afterTurn(target, func)
        
    def betweenTurns(self, func):
        """ Perform between turns """
        self.playerSide.betweenTurns()
        self.oppSide.betweenTurns()
        return []
        
    def checkFaint(self):
        """ Check if a Pokemon has fainted """
        messages = []
        
        messages += self.checkFaintOnSide(self.playerSide)
        if (self.over):
            return messages
            
        messages += self.checkFaintOnSide(self.oppSide)
        if (self.over):
            return messages
            
        return messages
        
    def checkFaintOnSide(self, side):
        """ Checks if a Pkmn on a side has fainted """
        messages = []
        
        if (side.pkmnInPlay[0].isFainted()):
            messages.append(side.pkmnInPlay[0].getHeader() + " fainted.")
            messages += self.checkOver(side)
        return messages
        
    def checkOver(self, side):
        """ Checks if the game is over """
        messages = []
        
        if (side.hasMorePokemon()):
            """ """
        else:
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