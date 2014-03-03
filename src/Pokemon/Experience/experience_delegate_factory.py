from Pokemon.Experience.experience_delegate import ExperienceDelegate
import Pokemon.Experience.Rates.experience_rate_factory as ExperienceRateFactory

from resources.tags import Tags

def loadFromXML(parent, tree):
    """  Build a Pokemon's Battle Information """
    currentExperience = int(tree.findtext(Tags.experienceTag))
    rateType = parent.species.rateType
    rate = ExperienceRateFactory.buildExperienceRate(rateType)
    
    return ExperienceDelegate(currentExperience, rate, parent)