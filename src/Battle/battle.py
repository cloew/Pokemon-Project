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
        
    def getActionsInOrder(self, screen):
        """ Returns all the Actions for this turn in the Battle """
        oppAction = self.oppSide.trainer.getAction(self.getOppPkmn()[0], self.getPlayerPkmn(), screen)
        playerAction = self.playerSide.trainer.getAction(self.getPlayerPkmn()[0], self.getOppPkmn(), screen)
        
        if self.doesPlayerGoFirst(playerAction, oppAction):
            return [playerAction, oppAction]
        else:
            return [oppAction, playerAction]
        
    def doesPlayerGoFirst(self, playerAction, oppAction):
        """ Compare action priorities to see who goes first """
        if playerAction.getPriority() == oppAction.getPriority():
            return self.doesPlayerGoFirstBySpeed()
        return playerAction.getPriority() > oppAction.getPriority()
    
    def doesPlayerGoFirstBySpeed(self):
        """ Compares Speeds to decide if the player goes first """
        oppSpeed = self.oppSide.pkmnInPlay[0].getStat("SPD")
        playerSpeed = self.playerSide.pkmnInPlay[0].getStat("SPD")
        
        if oppSpeed < playerSpeed:
            return True
        elif playerSpeed < oppSpeed:
            return False
        else:
            return random.randint(0,1)
                               
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
        
        if (self.playerSide.pkmnInPlay[0].isFainted()):
            messages.append(self.playerSide.pkmnInPlay[0].getHeader() + " fainted.")
        if (self.oppSide.pkmnInPlay[0].isFainted()):
            messages.append(self.oppSide.pkmnInPlay[0].getHeader() + " fainted.")
            
        message = self.checkOver()
        if message:
            messages.append(message)
            
        return messages
        
    def checkOver(self):
        """ Checks if the game is over """
        if (not self.playerSide.hasMorePokemon()):
            self.over = True
            return self.playerSide.trainer.name + " blacked out."
        if (not self.oppSide.hasMorePokemon()):
            self.over = True
            return "Defeated " +self.oppSide.trainer.name + "."
        
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