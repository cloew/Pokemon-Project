from Menu.menu_entry import MenuEntry

class TrainerMenuEntry(MenuEntry):
    """ Represents an entry in the menu """
    
    def __init__(self, trainer):
        """ Builds a trainer menu entry with its trainer """
        self.trainer = trainer
        self.selected = False
        
    def call(self):
        """ Trainer Entry ahs no function to call """
        
    def getTrianer(self):
        """ Returns the entry's trainer """
        return self.trainer
        