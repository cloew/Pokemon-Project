import xml.etree.ElementTree
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
        return PokemonDisplayDelegate(pkmn.species)
        
    @staticmethod
    def loadFromDB():
        """ AAAAAAAAAGGGGGGGGGGGHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!! """
                
    @staticmethod
    def copy(toCopy):
        """ Copies the Given Pkmn """
        return PokemonDisplayDelegate(toCopy.species)