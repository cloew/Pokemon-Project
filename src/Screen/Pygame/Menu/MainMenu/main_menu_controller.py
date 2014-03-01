from InputProcessor import commands
from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry

from kao_gui.pygame.pygame_controller import PygameController

from Screen.Pygame.Menu.MainMenu.main_menu_screen import MainMenuScreen
from Screen.Pygame.Marathon.marathon_controller import MarathonController
from Screen.Pygame.Menu.OptionsMenu.options_menu_controller import OptionsMenuController
from Screen.Pygame.Menu.TrainerMenu.trainer_menu_controller import TrainerMenuController

from Player.player_factory import PlayerFactory

class MainMenuController(PygameController):
    """ Controller for the Pygame Main Menu """
    
    def __init__(self):
        """ Initialize the Main Menu Controller """
        self.currentPlayer = PlayerFactory.getLastPlayer()
        
        
        entries = [TextMenuEntry("New", self.newGame),
                   TextMenuEntry("Options", self.runOptions),
                   TextMenuEntry("Exit", self.stopRunning)]
        self.menu = Menu(entries)
        
        if self.currentPlayer is not None:
            continueMenuEntry = TextMenuEntry("Continue", self.continueGame)
            entries.insert(1, continueMenuEntry)
            self.menu.down()
        
        screen = MainMenuScreen(self.menu, self.currentPlayer)
        PygameController.__init__(self, screen, commands = {commands.UP:self.menu.up,
                                                            commands.DOWN:self.menu.down,
                                                            commands.EXIT:self.stopRunning,
                                                            commands.SELECT:self.menu.enter})
        
    def newGame(self, entry):
        """ Start a New Game """
        PlayerFactory.createNewPlayer("Doe")
        
    def continueGame(self, entry):
        """ Continue the Game """
        self.runController(MarathonController(self.currentPlayer.trainer))
        # self.runController(TrainerMenuController())
        
    def runOptions(self, entry):
        """ Run Options Controller """
        self.runController(OptionsMenuController())