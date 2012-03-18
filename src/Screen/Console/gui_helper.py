CANCEL_LETTER = "/"

def PrintOppPokemon(pkmn):
    """ Prints a Pkmn to the console """
    print pkmn.getCurrHP(), "/", pkmn.getStat("HP"), \
             "\t", pkmn.getStatus().abbr, "\t", pkmn.name
             
def PrintPlayerPokemon(pkmn):
    """ Prints a Pkmn to the console """
    print pkmn.name, "\t", pkmn.getStatus().abbr, "\t", \
             pkmn.getCurrHP(),  "/", pkmn.getStat("HP")
             
def GetInput(validInput):
        """ Gets valid input from the user """
        valid = False
        while not valid:
            i = raw_input().strip()
            valid = ValidateInput(i, validInput)
        return i
        
def ValidateInput(input, validInput):
        """ Validates that input entered is valid """
        return input in validInput or input == CANCEL_LETTER