

class FaintHandlerDelegate:
    """ Class to handle whether an effect should continue based on
    whether the Pkmn involved have fainted """
    
    def cantHandle(self, user = None, target = None):
        """ Returns if the Effect cannot handle """
        return False
        