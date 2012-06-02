from Menu.menu import Menu
from Menu.menu_entry import MenuEntry

from Menu.OptionsMenu.options_menu_controller import OptionsMenuController

class MainMenu(Menu):
    """ Class to represent the main menu """
    
    def addEntries(self):
        """ Add Entries to the menu """
        self.entries = [MenuEntry("Start", self.startGame), 
                             MenuEntry("Options", self.options),
                             MenuEntry("Exit", self.quit)]
            
    def startGame(self):
        """ Start the game """
        print "Starting game"
        
    def options(self):
        """ Go to the options menu """
        options = OptionsMenuController()
        options.run()