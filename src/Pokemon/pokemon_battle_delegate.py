from Battle.Status.status import Status

class PokemonBattleDelegate:
    """ Holds a Pokemon's information with regards to battling
    Holds stats attacks and statuses """
  
    statKeys = ["HP", "ATK", "DEF", "SPD", "SATK", "SDEF"]
        
    def heal(self, heal):
        """ Has the Pokemon heal itself """
        self.currHP = self.currHP + int(heal)
        
        if self.currHP > self.stats["HP"]:
            self.currHP = self.stats["HP"]
        
    def takeDamage(self, damage):
        """ Has the Pokemon take damage """
        self.currHP = self.currHP - int(damage)
        
        if self.currHP <= 0:
            self.currHP = 0
        