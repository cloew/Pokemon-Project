from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry

#from Menu.OptionsMenu.options_menu_controller import OptionsMenuController
#from Menu.TrainerMenu.trainer_menu_controller import TrainerMenuController

class MainMenu(Menu):
    """ Class to represent the main menu """
    
    def addEntries(self):
        """ Add Entries to the menu """
        self.entries = [TextMenuEntry("Start", self.startGame), 
                        TextMenuEntry("Options", self.options),
                        TextMenuEntry("Exit", self.quit)]
            
    def startGame(self, entry):
        """ Start the game """
        trainerSelect = TrainerMenuController()
        trainerSelect.run()
        
    def options(self, entry):
        """ Go to the options menu """
        options = OptionsMenuController()
        options.run()