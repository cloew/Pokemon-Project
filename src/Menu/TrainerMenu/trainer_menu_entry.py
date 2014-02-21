from Menu.menu_entry import MenuEntry

from Trainer.trainer_factory import TrainerFactory

class TrainerMenuEntry(MenuEntry):
    """ Represents an entry in the menu """
    
    def __init__(self, trainer, callback):
        """ Builds a trainer menu entry with its trainer """
        self.trainer = trainer
        MenuEntry.__init__(self, callback)
        
    def getTrainer(self):
        """ Returns the entry's trainer """
        return self.trainer

    def getTextLength(self):
        """ Return the printable length of the Entry's Text """
        return len(self.getText())
        
    def getText(self):
        """ Return text to display for the Entry """
        return "{0} {1}".format(self.trainer.title, self.trainer.name)
        