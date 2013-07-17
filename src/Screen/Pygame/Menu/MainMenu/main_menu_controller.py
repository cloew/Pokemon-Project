from InputProcessor import commands
from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.MainMenu.main_menu_screen import MainMenuScreen
from Screen.Pygame.Menu.OptionsMenu.options_menu_controller import OptionsMenuController
from Screen.Pygame.Menu.TrainerMenu.trainer_menu_controller import TrainerMenuController

class MainMenuController(Controller):
    """ Controller for the Pygame Main Menu """
    
    def __init__(self):
        """ Initialize the Main Menu Controller """
        Controller.__init__(self)
        entries = [TextMenuEntry("Start", self.startGame),
                   TextMenuEntry("Options", self.runOptions),
                   TextMenuEntry("Exit", self.exit)]
        self.menu = Menu(entries)
        
        self.screen = MainMenuScreen(self.menu)
        self.cmds = {commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.EXIT:self.menu.quit,
                     commands.SELECT:self.menu.enter}
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.running
        
    def startGame(self, entry):
        """ Start the Game """
        trainerSelect = TrainerMenuController()
        trainerSelect.run()
        
    def runOptions(self, entry):
        """ Run Options Controller """
        options = OptionsMenuController()
        options.run()
        
    def exit(self, entry):
        """ Exit the controller """
        self.stopRunning()