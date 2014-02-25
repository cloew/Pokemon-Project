
class MediumSlowExperienceRate:
    """ Represents the Medium Slow Experience Rate Formula """
    
    def getExperinceForLevel(self, level):
        """ Return the experience needed for the given level """
        return int(1.2*(level**3) - 15*(level**2) + 100*level - 140)