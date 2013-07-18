from InputProcessor import commands
from Screen.Pygame.Battle.battle_message_box import BattleMessageBox
from Screen.Pygame.Controller.controller import Controller

class BattleAftermathController(Controller):
    """ Controller for Battle Aftermath """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Introduction Controller """
        Controller.__init__(self)
        self.battle = battle
        self.screen = screen
        self.screen.setBottomView(BattleMessageBox(self.battle))
        self.cmds = {commands.SELECT:self.battle.removeMessageFromQueue}
        
    def update(self):
        """ Tells the battle object what to perform """
        self.battle.update()
        if self.battle.noMessages():
            self.stopRunning()