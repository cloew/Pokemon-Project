from gui_helper import PrintPlayerPokemon, GetInput, CANCEL_LETTER
from resources.constants import Constants

class ConsoleSwitchScreen:
    """ Represents the Screen to switch Pkmn """
    validRange = ["1", "2", "3", "4", "5", "6"]
    
    def __init__(self, trainer, pkmnOut):
        """ Builds a screen to switch between Pokemon """
        self.trainer = trainer
        self.done = False
        
        self.pkmnToSwitch = pkmnOut[0]
        
        self.pkmnOut = []
        for pkmn in pkmnOut:
            self.pkmnOut.append(pkmn.pkmn)
        
    def switch(self):
        """ Gets a Pkmn to switch to """
        while not self.done:
            self.printScreen()
            i = GetInput(self.validRange[:len(self.trainer.beltPokemon)])
        
            if i == CANCEL_LETTER:
                return False, None
            pkmn = self.trainer.beltPokemon[int(i)-1]
            self.validatePkmn(pkmn)
            
        return True, [Constants.switchAction, self.pkmnToSwitch, pkmn]
        
    def printScreen(self):
        """ Prints a list of all the Pkmn the Trainer has out """
        i = 1
        print
        
        for pkmn in self.trainer.beltPokemon:
            print i,
            PrintPlayerPokemon(pkmn)
            i += 1
            
        print
        print "Which Pkmn will you switch to?\n"
        
        
    def validatePkmn(self, pkmn):
        """ Make sure the Pokemon is a valid choice """
        if pkmn.getStatus().abbr == "FNT":
            print pkmn.name, "has fainted."
            raw_input("Press 'Enter' to continue")
        
        elif pkmn in self.pkmnOut:
            print pkmn.name, "is already out."
            raw_input("Press 'Enter' to continue")
            
        else:
            self.done = True
            