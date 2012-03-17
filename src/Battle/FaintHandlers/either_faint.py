from Battle.FaintHandlers.faint_handler import FaintHandlerDelegate

class EitherFaintDelegate(FaintHandlerDelegate):
    """ Handler that can't handle eithe rpkmn fainting """
    
    def cantHandle(self, user = None, target = None):
        """ Returns if the Effect cannot handle the pkmn being fainted """
        return user.fainted() or target.fainted()