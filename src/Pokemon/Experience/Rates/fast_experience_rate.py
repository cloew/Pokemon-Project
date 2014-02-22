from medium_fast_experiece_rate import MediumFastExperienceRate

class FastExperience(MediumFastExperienceRate):
    """ Represents the Fast Experience Rate Formula """
    
    def getExperinceForLevel(self, level):
        """ Return the experience needed for the given level """
        return 4*MediumFastExperience.getExperinceForLevel(level)/5