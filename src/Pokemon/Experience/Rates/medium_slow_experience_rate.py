
class MediumSlowExperienceRate:
    """ Represents the Medium Slow Experience Rate Formula """
    
    def getExperinceForLevel(self, level):
        """ Return the experience needed for the given level """
        return int(6.0*(level**3)/5 + 15*(level**2) + 100*level - 140)