from Pokemon.Experience.experience_delegate import ExperienceDelegate

import Poekmon.Experience.species_factory as SpeciesFactory
import Poekmon.Experience.Rates.experience_rate_factory as ExperienceRateFactory

def loadFromXML(parent, tree):
    """  Build a Pokemon's Battle Information """
    currentExperience = int(tree.findtext(Tags.experienceTag))
    
    speciesXML = SpeciesFactory.loadSpeciesXML(parent.species)
    baseExperience = int(speciesXML.findtext(Tags.experienceTag))
    rateType = speciesXML.findtext(Tags.rateTypeTag)
    rate = ExperienceRateFactory.buildExperienceRate(rateType)
    
    return ExperienceDelegate(currentExperience, baseExperience, rate, parent)