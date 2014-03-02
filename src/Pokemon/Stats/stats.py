from Pokemon import species_factory as SpeciesFactory

from resources.tags import Tags

class Stats:
    """ Represents a Pokemon's Stats """
    statKeys = ["HP", "ATK", "DEF", "SPD", "SATK", "SDEF"]
    
    def __init__(self, parent):
        """ Initialize the Pokemon's stats """
        self.parent = parent
        self.currentHP = 0
        self.stats = {}
        self.loadStats()
        
    def levelUp(self):
        """ Level up the Pkmn's stats """
        originalHP = self.hp
        self.loadStats()
        self.currentHP += (self.hp-originalHP)
        
    def loadStats(self):
        """ Load Stats from the Pokedex XML file """
        for key in self.statKeys:
            baseStat = self.parent.species.baseStats[key]
            if (key is "HP"):
                self.stats[key] = self.calculateHPStat(baseStat)
            else:
                self.stats[key] = self.calculateStat(baseStat)
                
    def calculateHPStat(self, baseStat):
        """ Calculate the Current HP Stat """
        # ( (IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 10 + Level
        return int(((2*int(baseStat))*self.parent.level/100.0)+10 + self.parent.level )
        
    def calculateStat(self, baseStat):
        """ Calculate a Stat """
        # (((IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 5) * Nature Value
        return int(((2*int(baseStat))* self.parent.level/100.0) + 5)
        
    @property
    def hp(self):
        """ Return the HP Stat of the Pokemon """
        return self.stats["HP"]