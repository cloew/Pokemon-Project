from collections import deque
from Battle.battle_side import BattleSide
from Battle.Attack.attack import Attack
from Battle.battle_round import BattleRound
from Battle.battle_message import BattleMessage

import random

class Battle:
    """ Represents a Battle between two Trainers """
    
    def __init__(self, playerTrainer, oppTrainer):
        """ Builds the two participating sides of the battle """
        self.playerSide = BattleSide(playerTrainer)
        self.oppSide = BattleSide(oppTrainer)
        self.over = False
        self.round = BattleRound(self.playerSide, self.oppSide)
        self.battleFuncs = [self.performRound, self.refillSides]
        self.funcIndex = 0 # Ewww....
        self.messageQueue = deque()
        self.introduce()
        
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
                
    def introduce(self):
        """ Introduces the battle """
        messages = ["%s challenges you to a Pokemon Battle!" % self.getOppTrainer().getFullName()]
        messages += self.sendOutPkmnToStart()
        self.addMessages(messages)
                
    def update(self):
        """ Updates the Battle Object """
        if self.noMessages():
            self.battleFuncs[self.funcIndex]()
            self.funcIndex +=1
            self.funcIndex %= 2
            
    def noMessages(self):
        """ Returns if there are no messages in the message queue """
        return len(self.messageQueue) == 0
        
    def performRound(self):
        """  Performs a single round """
        self.round.run()
        self.betweenRounds()
        self.messageQueue += self.round.messageQueue
        
    def betweenRounds(self):
        """ Perform between rounds """
        self.playerSide.betweenRounds()
        self.oppSide.betweenRounds()
        return []
        
    def refillSides(self):
        """ Refills fainted Pkmn on each side """
        self.checkOver()
        if not self.over:
            messages = []
            messages += self.playerSide.refill()
            messages += self.oppSide.refill()
            self.addMessages(messages)
        
    def checkOver(self):
        """ Checks if the game is Over """
        self.checkOverForSide(self.playerSide)
        if not self.over:
            self.checkOverForSide(self.oppSide)
        
    def checkOverForSide(self, side):
        """ Checks if the game is over because the side has no Pkmn """
        if not side.hasPokemon():
            self.over = True
            self.addMessages([side.trainer.beaten()])
        
    def addMessages(self, messages):
        """ Adds the given messages to the message queue """
        battleMessages = []
        for message in messages:
            battleMessages.append(BattleMessage(message))
        
        self.messageQueue += deque(battleMessages)
        
    def getPlayerTrainer(self):
        """ Returns the Player Trainer """
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