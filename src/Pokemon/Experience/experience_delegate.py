
class ExperienceDelegate:
    """ Represents the Pokemon's Experience Delegate """
    
    def __init__(self, currentExperience, baseExperience, experienceRate, parent):
        """ Initialize the Experience Delegate """
        self.currentExperience = currentExperience
        self.baseExperience = baseExperience
        self.experieceRate = experienceRate
        self.parent = parent
    
    def gainExperience(self, experience):
        """ Gain experience """
        self.currentExperience += experience
    
    @property
    def experienceToAward(self):
        """ Return the experince to the next level """
        return (self.baseExperience*self.parent.level)/7
    
    @property
    def experinceToNextLevel(self):
        """ Return the experince to the next level """
        return self.experinceForNextLevel - self.currentExperience
        
    @property
    def experinceForNextLevel(self):
        """ Return the experince for the next level """
        return self.experienceRate.getExperinceForLevel(self.parent.level+1)