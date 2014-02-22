from medium_fast_experiece import MediumFastExperience

class FastExperience(MediumFastExperience):
    """ Represents the Fast Experience Formula """
    
    def getExperinceForLevel(self, level):
        """ Return the experience needed for the given level """
        return 4*MediumFastExperience.getExperinceForLevel(level)/5