from Menu.menu import Menu
from Menu.TrainerMenu.trainer_menu_entry import TrainerMenuEntry

from Trainer.trainer_factory import TrainerFactory

class TrainerMenu(Menu):
    """ Represents a menu in the game """
        
    def addEntries(self):
        """ Add Entries to the menu """
        self.entries = []
        playableTrainers = TrainerFactory.getPlayableTrainers()
        
        for trainer in playableTrainers:
            self.entries.append(TrainerMenuEntry(trainer))
            
    def enter(self):
        """ Call the selected entry """
        if self.entries != []:
            self.entries[self.current].call()