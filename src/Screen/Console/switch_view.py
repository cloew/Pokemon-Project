from gui_helper import PrintPlayerPokemon, GetInput, CANCEL_LETTER

class ConsoleSwitchScreen:
    """ Represents the Screen to switch Pkmn """
    validRange = ["1", "2", "3", "4", "5", "6"]
    
    def __init__(self, trainer, pkmn):
        """ Builds a screen to switch between Pokemon """
        self.trainer = trainer
        self.pkmn = pkmn
        
    def switch(self):
        """ Gets a Pkmn to switch to """
        self.printScreen()
        
        i = GetInput(self.validRange[:len(self.trainer.beltPokemon)])
        
        if i == CANCEL_LETTER:
            return False, None
        return True, None
        
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