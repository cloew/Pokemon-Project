from Battle.Status.status import Status

class PokemonBattleDelegate:
    """ Holds a Pokemon's information with regards to battling
    Holds stats attacks and statuses """
  
    statKeys = ["HP", "ATK", "DEF", "SPD", "SATK", "SDEF"]
  
    def getPokedexBattleInfo(self):
        """ Gets info from Pokedex relevanty to Battling
        Types, base stats """
        # Open Pokedex and set variables that require Pokedex data
        try:
            pokedex = open("resources/POKEDEX.txt", 'r')
        except IOError:
            print "Unable to open POKEDEX"
            exit(-2)
      
        temp = ""
        while (temp.find(self.parent.species) == -1):
            temp = pokedex.readline().strip()

        # Get type(s)
        self.types = pokedex.readline().strip().split(" ")
    
        # Get stats
        values = pokedex.readline().strip().split(" ")
        self.stats = {}
        for i in range(len(values)):
            key = PokemonBattleDelegate.statKeys[i]
            baseStat = values[i]
            if (key is "HP"):
                # ( (IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 10 + Level
                self.stats[key] = int(((2*int(baseStat))*self.parent.level/100.0)+10 + self.parent.level )
            else:
                # (((IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 5) * Nature Value
                self.stats[key] = int(((2*int(baseStat))* self.parent.level/100.0) + 5)
                
        
        pokedex.close()
            
    def buildStarter(self, parent):
        """ Builds a BattleDelegate for a Starter Pokemon """
        # Set parent
        self.parent = parent
    
        # Get common info from Pokedex 
        self.getPokedexBattleInfo()
    
        # Set currHP to full
        self.currHP = self.stats["HP"]
    
        # Load attacks
        self.attacks = []
        
        self.status = Status()
    
        return self
    
    
  
    def loadFromHumanTrainerFile(self, parent, file):
        """  Build a Pokemon's Battle Information """
        # Set parent
        self.parent = parent
    
        # Get Pokedex battle info on the Pokemon
        self.getPokedexBattleInfo()
    
        # Get current HP
        self.currHP = int(file.readline())
    
        # Read attacks
        numAttacks = int(file.readline())
        self.attacks = []
        for x in range(numAttacks):
            self.attacks.append(AttackFactory.loadFromPkmnXML(file))
        
        # Status
        self.status = Status()

        return self
        
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
        