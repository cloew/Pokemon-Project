from InputProcessor import commands
from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry

from kao_gui.pygame.pygame_controller import PygameController

from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.MainMenu.main_menu_screen import MainMenuScreen
from Screen.Pygame.Menu.OptionsMenu.options_menu_controller import OptionsMenuController
from Screen.Pygame.Menu.TrainerMenu.trainer_menu_controller import TrainerMenuController

class MainMenuController(PygameController):
    """ Controller for the Pygame Main Menu """
    
    def __init__(self):
        """ Initialize the Main Menu Controller """
        entries = [TextMenuEntry("Start", self.startGame),
                   TextMenuEntry("Options", self.runOptions),
                   TextMenuEntry("Exit", self.stopRunning)]
        self.menu = Menu(entries)
        
        screen = MainMenuScreen(self.menu)
        PygameController.__init__(self, screen, commands = {commands.UP:self.menu.up,
                                                            commands.DOWN:self.menu.down,
                                                            commands.EXIT:self.stopRunning,
                                                            commands.SELECT:self.menu.enter})
        
    def startGame(self, entry):
        """ Start the Game """
        self.runController(TrainerMenuController())
        
    def runOptions(self, entry):
        """ Run Options Controller """
        self.runController(OptionsMenuController())