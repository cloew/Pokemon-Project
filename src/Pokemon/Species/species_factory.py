from resources.resource_manager import GetResourcePath
from resources.tags import Tags

from Pokemon.Species.species import Species
from Pokemon.Stats.stats import Stats

from XML.xml_factory import XmlFactory

import xml.etree.ElementTree

class SpeciesFactory(XmlFactory):
    """ Represents the Species Factory """
    
    def __init__(self):
        """ Initialize the Species Factory """
        XmlFactory.__init__(self, "pokedex.xml")
        
    def getSpecies(self, species):
        """ Return the Species object for the given Species """
        speciesXML = self.loadSpeciesXML(species)
        baseExperience = int(speciesXML.findtext(Tags.experienceTag))
        rateType = speciesXML.findtext(Tags.rateTypeTag)
        
        baseStats = {}
        statsXML = speciesXML.find(Tags.baseStatsTag)
        for key in Stats.statKeys:
            baseStats[key] = int(statsXML.find(key).text)
            
        typesXML = speciesXML.find(Tags.typesTag)
        types = []
        for type in typesXML.getiterator(Tags.typeTag):
            types.append(type.text)
            
        return Species(species, types, baseStats, baseExperience, rateType)

    def loadSpeciesXML(self, species):
        """ Returns the XML tree for the pokemon with the species given """
        for pkmn in self.tree.getiterator(Tags.pokemonTag):
            if pkmn.find(Tags.speciesTag).text == species:
                return pkmn
                
SpeciesFactory = SpeciesFactory()