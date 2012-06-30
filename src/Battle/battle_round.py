from collections import deque

class BattleRound:
    """ Represents a single round of a battle """
    
    def __init__(self, playerSide, oppSide, screen):
        """ Build the Battle Round from its trainers """
        self.playerSide = playerSide
        self.oppSide = oppSide
        self.screen = screen
        self.messageQueue = deque()
        
    def run(self):
        """ Runs the Round """
        self.performActions()
        
    def performActions(self):
        """ Perform all the Round actions """
        actions = self.getActions()
        for action in actions:
            messages = []
            messages += self.act(action)
            messages += self.afterTurn(action.user)
            
            self.messageQueue.append(messages)
            #map(self.messageQueue.append, messages)
            self.messages = messages
            #self.screen.reportAction(messages)
        
    def getActions(self):
        """ Get all actions in the round """
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
        """ Perform affects of items/status/field hazards after the user performs its turn """
        return user.afterTurn()
        
    def getPlayerPkmn(self):
        """ Returns the Pokemon currently out """
        return self.playerSide.pkmnInPlay
        
    def getOppPkmn(self):
        """ Returns the Pokemon currently out """
        return self.oppSide.pkmnInPlay