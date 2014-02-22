
class ErraticExperience:
    """ Represents the Erratic Experience Formula """
    
    def getExperinceForLevel(self, level):
        """ Return the experience needed for the given level """
        intermediateAmount = 0
        if level < 50:
            intermediateAmount = self.below50(level)
        elif level <= 68:
            intermediateAmount = self.between50And68(level)
        elif level < 98:
            intermediateAmount = self.between68And98(level)
        else:
            intermediateAmount = self.above98(level)
            
        return int((level**3)*intermediateAmount)
        
    def below50(self, level):
        """ Return the experience when below level 15 """
        return (100-level)/50.0
        
    def between50And68(self, level):
        """ Return the experience when between level 15 and 36 """
        return (150-level)/100.0
        
    def between68And98(self, level):
        """ Return the experience when between level 15 and 36 """
        return ((1911-10*level)/3)/500.0
        
    def above98(self, level):
        """ Return the experience when above level 15 and 36 """
        return (160-level)/100.0