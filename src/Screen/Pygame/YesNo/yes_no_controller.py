from Battle.battle_message import BattleMessage
from InputProcessor import commands

from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController
from Screen.Pygame.YesNo.yes_no_screen import YesNoScreen

from kao_gui.pygame.pygame_controller import PygameController

class YesNoController(PygameController):
    """ Controller for picking Yes or No """
    
    def __init__(self, message, lastScreen):
        """ Initialize the Yes/No Controller """
        self.message = BattleMessage(message.message)
        self.lastScreen = lastScreen
        
        screen = YesNoScreen(lastScreen)
        cmds = {commands.SELECT:self.select,
                commands.EXIT:self.back}
        PygameController.__init__(self, screen, commands=cmds)
        
        self.answer = False
        self.displayedMessage = False
        
    def performGameCycle(self):
        """ Perform the learn attack loop """
        if not self.displayedMessage:
            controller = MessageBoxController(self.message, self.lastScreen, autoClose=True)
            self.screen.messageBox = controller.screen.messageBox
            self.runController(controller)
            self.displayedMessage = True
        
    def select(self):
        """ Select the current entry """
        self.answer = True
        self.stopRunning()
        
    def back(self):
        """ Return to the previous """
        self.answer = False
        self.stopRunning()