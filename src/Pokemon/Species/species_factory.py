from resources.resource_manager import GetResourcePath
from resources.tags import Tags

from XML.xml_factory import XmlFactory

import xml.etree.ElementTree

class SpeciesFactory(XmlFactory):
    """ Represents the Species Factory """
    
    def __init__(self):
        """ Initialize the Species Factory """
        XmlFactory.__init__(self, "pokedex.xml")

    def loadSpeciesXML(self, species):
        """ Returns the XML tree for the pokemon with the species given """
        for pkmn in self.tree.getiterator(Tags.pokemonTag):
            if pkmn.find(Tags.speciesTag).text == species:
                return pkmn
                
SpeciesFactory = SpeciesFactory()