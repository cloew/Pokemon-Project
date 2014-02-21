from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry
from Screen.Console.Menu.MainMenu.main_menu_screen import MainMenuScreen
from Screen.Console.Menu.OptionsMenu.options_menu_controller import OptionsMenuController

from kao_console.ascii import KAO_UP, KAO_DOWN, ENDL
from kao_gui.console.console_controller import ConsoleController

class MainMenuController(ConsoleController):
    """ Controller for the main menu """
    
    def __init__(self):
        """ Builds the Main Menu Controller """
        entries = [TextMenuEntry("Start", self.startGame),
                   TextMenuEntry("Options", self.runOptions),
                   TextMenuEntry("Exit", self.stopRunning)]
        self.menu = Menu(entries)
        
        screen = MainMenuScreen(self.menu)
        cmds = {KAO_UP:self.menu.up,
                KAO_DOWN:self.menu.down,
                ENDL:self.menu.enter}
                     
        ConsoleController.__init__(self, screen, commands=cmds)
        
    def startGame(self, entry):
        """ Start the Game """
        # self.runController(TrainerMenuController())
        
    def runOptions(self, entry):
        """ Run Options Controller """
        self.runController(OptionsMenuController())