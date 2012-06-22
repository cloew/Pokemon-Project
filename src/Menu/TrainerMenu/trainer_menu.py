from Menu.menu import Menu
from Menu.TrainerMenu.trainer_menu_entry import TrainerMenuEntry

class TrainerMenu(Menu):
    """ Represents a menu in the game """
    
    def __init__(self):
        """ Build the menu """
        self.running = True
        self.addEntries()
        self.current = 0
        self.selectEntry()
        
    def addEntries(self):
        """ Add Entries to the menu """
        self.entries = []
            
    def enter(self):
        """ Call the selected entry """
        if self.entries != []:
            """ Get Trainer and and start the actual game with it """