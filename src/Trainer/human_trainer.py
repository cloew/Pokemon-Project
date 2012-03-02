from Battle.Actions.action_factory import ActionFactory
from Battle.Actions.attack_action import AttackAction
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import random

class HumanTrainer(Trainer):
    """ Represents a Pokemon Trainer """
    header = ""
            
    def pickAction(self, user, targets, screen):
        """ Has the trainer pick its action via the screen """
        actionParams = self.screen.pickAction()
        return ActionFactory.buildActionFromType(actionParams)

    def getHeader(self):
        """ Return the header based on the type of trainer """
        return HumanTrainer.header
        
    def announcePkmn(self, pkmn):
        """ Announce a pkmn the trainer sends out """
        return "%s, I choose you!." % pkmn.name
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        return "You"