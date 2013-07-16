#from Menu.ActionMenu.action_controller import ActionController
#from Menu.ActionMenu.SwitchMenu.switch_controller import SwitchController
from Battle.Actions.action_factory import ActionFactory
from Battle.Actions.attack_action import AttackAction
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import random

class HumanTrainer(Trainer):
    """ Represents a Pokemon Trainer """
    header = ""
            
    def pickAction(self, user, targets, playerSide, oppSide, environment):
        """ Has the trainer pick its action via the screen """
        controller = ActionController(user, targets, playerSide, oppSide, environment)
        controller.run()
        return controller.menu.action

    def getHeader(self):
        """ Return the header based on the type of trainer """
        return HumanTrainer.header
        
    def announcePkmn(self, pkmn):
        """ Announce a pkmn the trainer sends out """
        return "%s, I choose you!" % pkmn.name
        
    def choosePokemon(self, pkmnInPlay):
        """ Returns a Pkmn chosen by the Trainer """
        controller = SwitchController(pkmnInPlay[0])
        controller.run()
        return controller.menu.action.pkmnToSwitchTo
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        return "You"
        
    def beaten(self):
        """ Returns a string that tells that the Trainer was beaten in Battle """
        return self.name + " blacked out."