from Battle.FaintHandlers.faint_handler import FaintHandlerDelegate

class UserFaintDelegate(FaintHandlerDelegate):
    """ Handler that can't handle user fainting """
    
    def cantHandle(self, user = None, target = None):
        """ Returns if the Effect cannot handle the pkmn being fainted """
        return user.fainted()