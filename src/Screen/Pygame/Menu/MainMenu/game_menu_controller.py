from InputProcessor import commands
from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry

from Screen.Pygame.Menu.MainMenu.main_menu_screen import MainMenuScreen
from Screen.Pygame.Marathon.marathon_controller import MarathonController

from kao_gui.pygame.pygame_controller import PygameController

class GameMenuController(PygameController):
    """ Controller for a picking the Game Mode """
    
    def __init__(self, currentPlayer):
        """ Initialize the Main Menu Controller """
        self.currentPlayer = currentPlayer
        
        
        entries = [TextMenuEntry("Story", self.playStory),
                   TextMenuEntry("Marathon", self.runMarathon),
                   TextMenuEntry("Back", self.stopRunning)]
        self.menu = Menu(entries)
        
        screen = MainMenuScreen(self.menu, self.currentPlayer)
        PygameController.__init__(self, screen, commands = {commands.UP:self.menu.up,
                                                            commands.DOWN:self.menu.down,
                                                            commands.EXIT:self.stopRunning,
                                                            commands.SELECT:self.menu.enter})
                                                            
    def playStory(self, entry):
        """ Play the Story Mode """
        print "Playing Story mode"
        
    def runMarathon(self, entry):
        """ Run a marathon """
        self.runController(MarathonController(self.currentPlayer.trainer))