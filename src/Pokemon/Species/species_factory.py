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
        
    def getSpecies(self, speciesName):
        """ Return the Species object for the given Species """
        speciesXML = self.loadSpeciesXML(speciesName)
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
            
        species = Species(speciesName, types, baseStats, baseExperience, rateType)
        self.loadAttacks(species, speciesXML)
        return species
        
    def loadAttacks(self, species, speciesXML):
        """ Load attacks """
        attacksXML = speciesXML.find(Tags.attacksTag)
        for attackXML in attacksXML.findall(Tags.attackTag):
            attackName = attackXML.findtext(Tags.nameTag)
            level = int(attackXML.findtext(Tags.levelTag))
            species.addAttack(attackName, level)

    def loadSpeciesXML(self, speciesName):
        """ Returns the XML tree for the pokemon with the species given """
        for pkmn in self.tree.getiterator(Tags.pokemonTag):
            if pkmn.findtext(Tags.speciesTag) == speciesName:
                return pkmn
                
SpeciesFactory = SpeciesFactory()