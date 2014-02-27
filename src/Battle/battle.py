from collections import deque
from Battle.battle_side import BattleSide
from Battle.Attack.attack import Attack
from Battle.battle_environment import BattleEnvironment
from Battle.battle_round import BattleRound
from Battle.battle_message import BattleMessage

class Battle:
    """ Represents a Battle between two Trainers """
    
    def __init__(self, playerTrainer, oppTrainer):
        """ Builds the two participating sides of the battle """
        self.playerSide = BattleSide(playerTrainer)
        self.oppSide = BattleSide(oppTrainer)
        self.environment = BattleEnvironment()
        self.over = False
        self.round = BattleRound(self.playerSide, self.oppSide, self.environment)
        self.messageQueue = deque()
        self.introduce()
        
    def introduce(self):
        """ Introduces the battle """
        messages = ["%s challenges you to a Pokemon Battle!" % self.getOppTrainer().getFullName()]
        messages += self.sendOutPkmnToStart()
        self.addMessages(messages)
        
    def sendOutPkmnToStart(self):
        """ Sends out Pkmn on both sides """
        messages = []
        messages += self.oppSide.sendOutPkmnAtStart()
        messages += self.playerSide.sendOutPkmnAtStart()
        return messages
        
    def removeMessageFromQueue(self, event=None):
        """ Pops a message from the message queue if it has been fully displayed """
        if len(self.messageQueue) > 0:
            if self.messageQueue[0].fullyDisplayed:
                self.messageQueue.popleft()

    def update(self):
        """ Update the Battle object """
        
    def performRound(self, alreadySelectedActions):
        """  Performs a single round """
        self.round.run(alreadySelectedActions)
        self.addMessages(self.round.messages)
        self.addMessages(self.betweenRounds())
        
    def betweenRounds(self):
        """ Perform between rounds """
        self.playerSide.betweenRounds()
        self.oppSide.betweenRounds()
        return self.environment.betweenRounds(self.playerSide, self.oppSide)
        
    def refillSides(self, pokemonReplacements):
        """ Refills fainted Pkmn on each side """
        self.checkOver()
        if not self.over:
            messages = self.playerSide.refill(pokemonReplacements)
            messages += self.oppSide.refill(pokemonReplacements)
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
            self.addMessages([side.trainer.getBeatenMessage()])
        
    def addMessages(self, messages):
        """ Adds the given messages to the message queue """
        battleMessages = []
        for message in messages:
            battleMessages.append(BattleMessage(message))
        
        self.messageQueue += deque(battleMessages)
        
    def noMessages(self):
        """ Returns if there are no messages in the message queue """
        return len(self.messageQueue) == 0
        
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