from experience_rate import ExperienceRate

class FluctuatingExperienceRate(ExperienceRate):
    """ Represents the Fluctuating Experience Rate Formula """
    
    def getExperinceFromFormula(self, level):
        """ Return the experience needed for the given level """
        intermediateAmount = 0
        if level < 15:
            intermediateAmount = self.below15(level)
        elif level <= 36:
            intermediateAmount = self.between15And36(level)
        else:
            intermediateAmount = self.above36(level)
            
        return ((level**3)*intermediateAmount)/50
        
    def below15(self, level):
        """ Return the experience when below level 15 """
        return (level+1)/3+24
        
    def between15And36(self, level):
        """ Return the experience when between level 15 and 36 """
        return level+14
        
    def above36(self, level):
        """ Return the experience when above level 15 and 36 """
        return level/2 +32