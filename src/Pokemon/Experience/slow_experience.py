from medium_fast_experiece import MediumFastExperience

class SlowExperience(MediumFastExperience):
    """ Represents the Medium Fast Experience Formula """
    
    def getExperinceForLevel(self, level):
        """ Return the experience needed for the given level """
        return 5*MediumFastExperience.getExperinceForLevel(level)/4