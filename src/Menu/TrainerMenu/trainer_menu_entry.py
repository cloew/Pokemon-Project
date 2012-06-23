from Menu.menu_entry import MenuEntry

class TrainerMenuEntry(MenuEntry):
    """ Represents an entry in the menu """
    
    def __init__(self, trainer):
        """ Builds a trainer menu entry with its trainer """
        self.trainer = trainer
        self.selected = False
        
    def call(self):
        """ Trainer Entry has no function to call """
        
    def getTrainer(self):
        """ Returns the entry's trainer """
        return self.trainer
        
    def getText(self):
        """ Return text to display for the Entry """
        return "{0} {1}".format(self.trainer.title, self.trainer.name)
        