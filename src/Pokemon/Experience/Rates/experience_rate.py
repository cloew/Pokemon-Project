
class ExperienceRate:
    """ Represents an Experince Rate Formula """
    
    def getExperinceForLevel(self, level):
        """ Return the experience needed for the given level """
        if level == 1:
            return 0
        else:
            return self.getExperinceFromFormula(level)
        
    def getExperinceFromFormula(self, level):
        """ Return the experience needed for the given level """
        return NotImplemented