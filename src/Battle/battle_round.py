from collections import deque

class BattleRound:
    """ Represents a single round of a battle """
    
    def __init__(self, playerSide, oppSide, environment):
        """ Build the Battle Round from its trainers """
        self.playerSide = playerSide
        self.oppSide = oppSide
        self.environment = environment
        self.messageQueue = deque()
        
    def run(self, alreadySelectedActions):
        """ Runs the Round """
        self.performActions(alreadySelectedActions)
        
    def performActions(self, alreadySelectedActions):
        """ Perform all the Round actions """
        self.messages = []
        actions = self.getActions(alreadySelectedActions)
        for action in actions:
            messages = []
            messages += self.act(action)
            messages += self.afterTurn(action.user)
            
            self.messageQueue += deque(messages)
            self.messages += messages
        
    def getActions(self, alreadySelectedActions):
        """ Get all actions in the round """
        oppAction = self.getActionForPokemon(self.getOppPkmn()[0], self.getPlayerPkmn(), alreadySelectedActions)
        playerAction = self.getActionForPokemon(self.getPlayerPkmn()[0], self.getOppPkmn(), alreadySelectedActions)
        
        actions = [oppAction] + [playerAction]
        actions.sort(reverse = True)
        return actions
        
    def getActionForPokemon(self, pokemon, targets, alreadySelectedActions):
        """ Return the action for the given pokemon """
        if pokemon in alreadySelectedActions:
            action = alreadySelectedActions[pokemon]
        else:
            action = pokemon.getTrainer().getAction(pokemon, targets, self.playerSide, self.oppSide, self.environment)
        return action
        
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