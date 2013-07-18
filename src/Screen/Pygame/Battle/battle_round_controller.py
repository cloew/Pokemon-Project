from InputProcessor import commands
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.ActionMenu.action_menu_controller import ActionMenuController

class BattleRoundController(Controller):
    """ Controller for Battle Rounds """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Round Controller """
        Controller.__init__(self)
        self.battle = battle
        self.screen = screen
        self.cmds = {commands.SELECT:self.battle.removeMessageFromQueue}
        
    def update(self):
        """ Tells the battle object what to perform """
        actionMenuController = ActionMenuController(self.battle, self.screen)
        actionMenuController.run()
        
        self.battle.update()
        if self.battle.noMessages():
            self.battle.performRound()
            
        if self.battle.over:
            self.stopRunning()