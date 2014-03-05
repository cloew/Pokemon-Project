from InputProcessor import commands

from Screen.Pygame.Battle.battle_message_box import BattleMessageBox
from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController

from kao_gui.pygame.pygame_controller import PygameController

class BattleIntroductionController(PygameController):
    """ Controller for Battle Introductions """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Introduction Controller """
        self.battle = battle
        PygameController.__init__(self, screen)
        
    def performGameCycle(self):
        """ Tells the battle object what to perform """
        while not self.battle.noEvents():
            event = self.battle.eventQueue.popleft()
            self.runController(MessageBoxController(event, self.screen))
        self.stopRunning()