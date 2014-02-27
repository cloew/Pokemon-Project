from experience_rate import ExperienceRate

class MediumFastExperienceRate(ExperienceRate):
    """ Represents the Medium Fast Experience Rate Formula """
    
    def getExperinceFromFormula(self, level):
        """ Return the experience needed for the given level """
        return level**3