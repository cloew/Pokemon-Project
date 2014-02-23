from Trainer.trainer import Trainer

import random

class HumanTrainer(Trainer):
    """ Represents a Pokemon Trainer """
    header = ""
            
    def pickAction(self, user, targets, playerSide, oppSide, environment):
        """ Has the trainer pick its action via the screen """
        print "Called human trainer PickAction"
        return None # This method should never be called, since the UI should eb used to select the Attack before the Round begins

    def getHeader(self):
        """ Return the header based on the type of trainer """
        return HumanTrainer.header
        
    def announcePkmn(self, pkmn):
        """ Announce a pkmn the trainer sends out """
        return "%s, I choose you!" % pkmn.name
        
    def choosePokemon(self, pkmnInPlay):
        """ Returns a Pkmn chosen by the Trainer """
        print "Called human trainer choosePokemon"
        return None # This emthod should never be called because choosing a Pkmn should be done from UI
        
    def getFullName(self):
        """ Return the full Name and Title of the trainer """
        return "You"
        
    def beaten(self):
        """ Returns a string that tells that the Trainer was beaten in Battle """
        return self.name + " blacked out."