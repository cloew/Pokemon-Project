from Battle.Actions.action_factory import ActionFactory
from Battle.battle import Battle
from Screen.Console.battle_view import ConsoleBattleScreen

class BattleViewController:
    """ Controls the interaction between the visible Screen and a battle 
    between two Trainers """
    
    def __init__(self):
        """  """
        
        
    def begin(self, playerTrainer, oppTrainer):
        """ Starts showing the Battle Screen and initializes the Battle """
        self.battle = Battle(playerTrainer, oppTrainer)
        self.screen = ConsoleBattleScreen(self.battle)
        
        # Set the Player Trainer to use the screen
        playerTrainer.screen = self.screen
        
        # Introduce the Battle Environment
        self.screen.introduce()
        messages = self.battle.sendOutPkmnToStart()
        self.screen.reportMessages(messages)
        
        # Start the Game Loop
        self.gameLoop()
        
    def gameLoop(self):
        """ Runs through one iteration if the game """
        while not self.battle.over:
            # Pick action
            actions = self.battle.getActionsInOrder()
            self.performActions(actions)
            messages = self.battle.refillSides()
            self.screen.reportAction(messages)
                    
    def performActions(self, actions):
        """ Perform all the given actions """
        for action in actions:
            messages = []
            messages += self.battle.act(action)
            messages += self.battle.afterTurn(action.user)
            
            self.screen.reportAction(messages)
            
        self.battle.betweenTurns()
        
    def checkOver(self):
        """ Checks if the Battle is over """
        return self.battle.over
        