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
        self.eventQueue = deque()
        self.introduce()
        
    def introduce(self):
        """ Introduces the battle """
        events = ["%s challenges you to a Pokemon Battle!" % self.getOppTrainer().getFullName()]
        events += self.sendOutPkmnToStart()
        self.addEvents(events)
        
    def sendOutPkmnToStart(self):
        """ Sends out Pkmn on both sides """
        events = []
        events += self.oppSide.sendOutPkmnAtStart()
        events += self.playerSide.sendOutPkmnAtStart()
        return events
        
    def removeEventFromQueue(self, event=None):
        """ Pops a message from the message queue if it has been fully displayed """
        if len(self.eventQueue) > 0:
            if self.eventQueue[0].fullyDisplayed:
                self.eventQueue.popleft()

    def update(self):
        """ Update the Battle object """
        
    def performRound(self, alreadySelectedActions):
        """  Performs a single round """
        self.round.run(alreadySelectedActions)
        self.addEvents(self.round.events)
        self.addEvents(self.betweenRounds())
        
    def betweenRounds(self):
        """ Perform between rounds """
        self.playerSide.betweenRounds()
        self.oppSide.betweenRounds()
        return self.environment.betweenRounds(self.playerSide, self.oppSide)
        
    def refillSides(self, pokemonReplacements):
        """ Refills fainted Pkmn on each side """
        self.checkOver()
        if not self.over:
            events = self.playerSide.refill(pokemonReplacements)
            events += self.oppSide.refill(pokemonReplacements)
            self.addEvents(events)
        
    def checkOver(self):
        """ Checks if the game is Over """
        self.checkOverForSide(self.playerSide)
        if not self.over:
            self.checkOverForSide(self.oppSide)
        
    def checkOverForSide(self, side):
        """ Checks if the game is over because the side has no Pkmn """
        if not side.hasPokemon():
            self.over = True
            self.addEvents([side.trainer.getBeatenMessage()])
        
    def addEvents(self, events):
        """ Adds the given events to the event queue """
        battleEvents = []
        for event in events:
            if type(event) is str:
                battleEvents.append(BattleMessage(event))
            else:
                battleEvents.append(event)
        
        self.eventQueue += deque(battleEvents)
        
    def noEvents(self):
        """ Returns if there are no events in the event queue """
        return len(self.eventQueue) == 0
        
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