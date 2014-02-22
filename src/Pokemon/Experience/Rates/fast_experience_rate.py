from medium_fast_experience_rate import MediumFastExperienceRate

class FastExperienceRate(MediumFastExperienceRate):
    """ Represents the Fast Experience Rate Formula """
    
    def getExperinceForLevel(self, level):
        """ Return the experience needed for the given level """
        return 4*MediumFastExperience.getExperinceForLevel(level)/5