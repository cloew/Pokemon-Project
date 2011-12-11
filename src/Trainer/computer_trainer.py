from Battle.Actions.attack_action import AttackAction
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import random

class ComputerTrainer(Trainer):
    """ Represents a Pokemon Trainer """
    header = "Enemy "
                
    def getAction(self, currPokemon):
        """ Get action, randomly pick an available attack """
        if self.actionLock:
            action = self.actionLock.useAction()
        else:
            action = self.pickAction(currPokemon)
            
            
        return action
        
    def pickAction(self, currPokemon):
        """ Has the computer pick its action """
        attacks = currPokemon.battleDelegate.attacks
        return  AttackAction(attacks[random.randint(0, len(attacks)-1)])
        
    def getHeader(self):
        """ Return the header based on the type of trainer """
        return ComputerTrainer.header
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        return "%s %s" % (self.title, self.name)