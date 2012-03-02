from Battle.Actions.attack_action import AttackAction
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import random

class ComputerTrainer(Trainer):
    """ Represents a Pokemon Trainer """
    header = "Enemy "
                
    def getAction(self, user, targets, screen):
        """ Get action, randomly pick an available attack """
        if user.actionLock:
            action = self.actionLock.useAction()
        else:
            action = self.pickAction(user, targets)
            
            
        return action
        
    def pickAction(self, user, targets, screen):
        """ Has the computer pick its action """
        attacks = user.getAttacks()
        attack = random.choice(attacks)
        target = random.choice(targets)
        return  AttackAction(attack, user, target)
        
    def getHeader(self):
        """ Return the header based on the type of trainer """
        return ComputerTrainer.header
        
    def announcePkmn(self, pkmn):
        """ Announce a pkmn the trainer sends out """
        return "%s sends out %s." % (self.getFullName(), pkmn.name)
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        return "%s %s" % (self.title, self.name)