
class Species:
    """ Represents a Pokemon Species """
    
    def __init__(self, name, types, baseStats, baseExperience, rateType):
        """ Initialize the Species """
        self.name = name
        self.types = types
        self.baseStats = baseStats
        self.baseExperience = baseExperience
        self.rateType = rateType