from medium_fast_experience_rate import MediumFastExperienceRate

class SlowExperienceRate(MediumFastExperienceRate):
    """ Represents the Slow Experience Rate Formula """
    
    def getExperinceForLevel(self, level):
        """ Return the experience needed for the given level """
        return 5*MediumFastExperience.getExperinceForLevel(level)/4