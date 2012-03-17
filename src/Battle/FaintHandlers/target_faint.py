from Battle.FaintHandlers.faint_handler import FaintHandlerDelegate

class TargetFaintDelegate(FaintHandlerDelegate):
    """ Handler that can't handle target fainting """
    
    def cantHandle(self, user = None, target = None, effect = None):
        """ Returns if the Effect cannot handle the pkmn being fainted """
        return target.fainted()