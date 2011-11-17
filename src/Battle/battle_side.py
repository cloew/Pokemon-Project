from Trainer.trainer import Trainer

class BattleSide:
    """ Holds the data for a side of a battle """
    
    def __init__(self, trainer):
        """  """
        self.trainer = trainer
        self.currPokemon = trainer.getFirstPokemon()
        self.statMods = {"ATK":0, "DEF":0, "SPD":0, "SATK":0, "SDEF":0, 
                                "ACC":0, "EVAS":0, "CRT":0}
                                
        self.flinching = False
        
        self.encore = 0
        
        self.lastAction = None
        self.dodge = None
        
        self.secondaryEffects = []
        
    def hasMorePokemon(self):
        """ Returns whether this side has more Pokemon """
        return self.trainer.hasMorePokemon()
        
    def resetStatMods(self):
        """ Resets the stat mods for the side """
        for key in self.statMods:
            self.statMods[key] = 0
            
    def afterTurn(self, func):
        """ Perform affects of items/status/field hazards after the acting side performs its turn """
        messages = self.currPokemon.getStatus().afterTurn(self)
        if func(messages):
            return
        
        for effect in  self.secondaryEffects:
            messages = effect.afterTurn(self)
            if func(messages):
                return

        
    def betweenTurns(self):
        """ Perform between turns """
        self.flinching = False
        
    def getHeader(self):
        """ Returns the string header based on the trainer and current Pokemon """
        return self.trainer.getHeader() + self.currPokemon.name