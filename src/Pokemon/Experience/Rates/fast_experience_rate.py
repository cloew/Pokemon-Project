from medium_fast_experience_rate import MediumFastExperienceRate

class FastExperienceRate(MediumFastExperienceRate):
    """ Represents the Fast Experience Rate Formula """
    
    def getExperinceFromFormula(self, level):
        """ Return the experience needed for the given level """
        return 4*MediumFastExperience.getExperinceFromFormula(level)/5