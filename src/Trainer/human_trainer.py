from Menu.ActionMenu.action_controller import ActionController
from Battle.Actions.action_factory import ActionFactory
from Battle.Actions.attack_action import AttackAction
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import random

class HumanTrainer(Trainer):
    """ Represents a Pokemon Trainer """
    header = ""
            
    def pickAction(self, user, targets):
        """ Has the trainer pick its action via the screen """
        #actionParams = self.screen.pickAction()
        #return ActionFactory.buildActionFromType(actionParams)
        controller = ActionController(None)
        controller.run()

    def getHeader(self):
        """ Return the header based on the type of trainer """
        return HumanTrainer.header
        
    def announcePkmn(self, pkmn):
        """ Announce a pkmn the trainer sends out """
        return "%s, I choose you!" % pkmn.name
        
    def choosePokemon(self, pkmnInPlay):
        """ Returns a Pkmn chosen by the Trainer """
        valid, params = self.screen.switch()
        return params[2]
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        return "You"
        
    def beaten(self):
        """ Returns a string that tells that the Trainer was beaten in Battle """
        return self.name + " blacked out."