from Battle.FaintHandlers.faint_handler import FaintHandlerDelegate

class AffectUserFaintDelegate(FaintHandlerDelegate):
    """ Handler that can't handle the affected pkmn fainting """
    
    def cantHandle(self, user = None, target = None, effect = None):
        """ Returns if the Effect cannot handle the pkmn being fainted """
        pkmn= effect.getEffectedPokemon(user, target)
        return pkmn.fainted()