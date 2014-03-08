from Battle.battle_message import BattleMessage
from InputProcessor import commands
from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry

from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController
from Screen.Pygame.YesNo.yes_no_screen import YesNoScreen

from kao_gui.pygame.pygame_controller import PygameController

class YesNoController(PygameController):
    """ Controller for picking Yes or No """
    
    def __init__(self, message, lastScreen):
        """ Initialize the Yes/No Controller """
        self.message = BattleMessage(message.message)
        self.lastScreen = lastScreen
        
        entries = [TextMenuEntry("Yes", self.select),
                   TextMenuEntry("No", self.back)]
        self.menu = Menu(entries)
        
        screen = YesNoScreen(self.menu, lastScreen)
        cmds = {commands.UP:self.menu.up,
                commands.DOWN:self.menu.down,
                commands.SELECT:self.menu.enter,
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
        
    def select(self, entry=None):
        """ Select the current entry """
        self.answer = True
        self.stopRunning()
        
    def back(self, entry=None):
        """ Return to the previous """
        self.answer = False
        self.stopRunning()