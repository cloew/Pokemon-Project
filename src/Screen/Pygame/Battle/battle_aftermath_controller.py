from InputProcessor import commands
from Screen.Pygame.Battle.battle_message_box import BattleMessageBox

from kao_gui.pygame.pygame_controller import PygameController

class BattleAftermathController(PygameController):
    """ Controller for Battle Aftermath """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Aftermath Controller """
        self.battle = battle
        screen.setBottomView(BattleMessageBox(self.battle, self.getWindow().width*.9, self.getWindow().height*.3))
        cmds = {commands.SELECT:self.battle.removeMessageFromQueue}
        PygameController.__init__(self, screen, commands=cmds)
        
    def performGameCycle(self):
        """ Tells the battle object what to perform """
        self.battle.update()
        if self.battle.noMessages():
            self.stopRunning()