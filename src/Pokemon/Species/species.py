
class Species:
    """ Represents a Pokemon Species """
    
    def __init__(self, name, types, baseStats, baseExperience, rateType):
        """ Initialize the Species """
        self.name = name
        self.types = types
        self.baseStats = baseStats
        self.baseExperience = baseExperience
        self.rateType = rateType
        
        self.attacksForLevel = {}
        
    def addAttack(self, attack, level):
        """ Add an Attack to be learned at the given level """
        if level in self.attacksForLevel:
            self.attacksForLevel[level].append(attack)
        else:
            self.attacksForLevel[level] = [attack]