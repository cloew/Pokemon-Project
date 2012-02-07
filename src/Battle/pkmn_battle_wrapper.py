
class PkmnBattleWrapper:
    """ Represents one Pkmn's slot in a battle """
    
    def __init__(self, side):
        """ Build the Pkmn Wrapper """
        self.side = side
        self.pkmn = None
        #self.trainer = trainer # May add back later if I decide to have mulitple trainers on the same side in a battle
        
        self.statMods = {"ATK":0, "DEF":0, "SPD":0, "SATK":0, "SDEF":0, 
                                "ACC":0, "EVAS":0, "CRT":0}
                                
        self.flinching = False
        self.encore = 0
        
        self.lastAction = None
        self.actionLock = None
        self.dodge = None
        
        self.secondaryEffects = []
        
    def sendOutPkmn(self, pkmn):
        """ Sends out the wrapper's pkmn """
        self.pkmn = pkmn
        return self.side.trainer.announcePkmn(pkmn)
        
    def resetStatMods(self):
        """ Resets the stat mods for the side """
        for key in self.statMods:
            self.statMods[key] = 0
            
    def afterTurn(self, func, otherSide):
        """ Perform affects of items/status/field hazards after the acting side performs its turn """
        messages = self.pkmn.ability.afterTurn(self, otherSide)
        if func(messages):
            return
            
        messages = self.pkmn.getStatus().afterTurn(self)
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
        return self.side.trainer.getHeader() + self.pkmn.name
        
        
    # Pokemon Accessors
    
    def getAbility(self):
        """ Returns the Wrapper's Pokemon's Ability """
        return self.pkmn.ability
        
    def takeDamage(self, damage):
        """ Has the Pkmn take the given amount of damage """
        self.pkmn.takeDamage(damage)
        
    def getLevel(self):
        """ Returns the Wrapper's POkemon's Level """
        return self.pkmn.level
        
    def getStat(self, stat):
        """ Returns the Wrapper's Pokemon's stat """
        return self.pkmn.getStat(stat)
        
    def getStatus(self):
        """ Returns the Wrapper's Pokemon's Status """
        return self.pkmn.getStatus()
        
    def setStatus(self, status):
        """ Sets the Wrapper's Pokemon's Status """
        self.pkmn.setStatus(status)
        
    def getTypes(self):
        """ Returns the Wrapper's Pokemon's Types """
        return self.pkmn.getTypes()