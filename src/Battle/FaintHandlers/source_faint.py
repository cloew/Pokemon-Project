from Battle.FaintHandlers.faint_handler import FaintHandlerDelegate

class SourceFaintDelegate(FaintHandlerDelegate):
    """ Handler that can't handle user or source fainting """
    
    def cantHandle(self, user = None, target = None, effect = None):
        """ Returns if the Effect cannot handle the pkmn being fainted """
        return self.checkSource(user, effect) or user.fainted()
        
    def checkSource(self, user, effect):
        """ Check if the source has fainted """
        srcFainted = effect.source.fainted()
        if srcFainted:
            self.removeEffect(user, effect)
            
        return srcFainted
        
    def removeEffect(self, user, effect):
        """ Removes the Effect from the user """
        user.secondaryEffects.remove(effect)