from Pokemon.DisplayDelegate.alternate_display_delegate import AlternateDisplayDelegate
from Pokemon.DisplayDelegate.pokemon_display_delegate import PokemonDisplayDelegate

from resources.tags import Tags

class PokemonDisplayDelegateFactory:
    """ Factory to build Pokemon Display Delegates """
    
    @staticmethod
    def buildStarter(species):
        """ Creates a Starter Pokemon's Display Delegate """
        return PokemonDisplayDelegate(species)
    
    @staticmethod
    def loadFromXML(tree, pkmn):
        """ Loads a Pokemon object from a file """
        if tree is None:
            print "Returning default Display Delegate for", pkmn.name
            return PokemonDisplayDelegate(pkmn.species)
        else:
            print "Returning alternate Display Delegate for", pkmn.name
            return AlternateDisplayDelegate(tree.text)
        
    @staticmethod
    def loadFromDB():
        """ AAAAAAAAAGGGGGGGGGGGHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!! """
                
    @staticmethod
    def copy(toCopy):
        """ Copies the Given Pkmn """
        return toCopy.displayDelegate