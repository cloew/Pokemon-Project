from Menu.menu_entry import MenuEntry
from Battle.battle_controller import BattleController

from Trainer.trainer_factory import TrainerFactory

class TrainerMenuEntry(MenuEntry):
    """ Represents an entry in the menu """
    
    def __init__(self, trainer):
        """ Builds a trainer menu entry with its trainer """
        self.trainer = trainer
        self.selected = False
        
    def call(self):
        """ Trainer Entry has no function to call """
        print "{0} {1}'s first Pkmn is {2}".format(self.trainer.title, self.trainer.name, self.trainer.beltPokemon[0].name)
        enemy = TrainerFactory.loadFromXML("Badass", "Eric", TrainerFactory.COMPUTER)
        controller = BattleController(self.trainer, enemy)
        controller.run()
        
    def getTrainer(self):
        """ Returns the entry's trainer """
        return self.trainer
        
    def getText(self):
        """ Return text to display for the Entry """
        return "{0} {1}".format(self.trainer.title, self.trainer.name)
        