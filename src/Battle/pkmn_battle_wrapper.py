from Battle.Status.statusfactory import StatusFactory

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
            
    def afterTurn(self, target):
        """ Perform affects of items/status/field hazards after the acting side performs its turn """
        messages = []
        afterTurnEffects = [self.getAbility(), self.getStatus()]
        afterTurnEffects += self.secondaryEffects
        
        for effect in  afterTurnEffects:
            messages += effect.attemptAfterTurn(self)
         
        return messages
        
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
        
    def getAttacks(self):
        """ Returns the Wrapper's Pokemon's Attacks """
        return self.pkmn.getAttacks()
        
    def heal(self, amount):
        """ Heal the Wrapper's Pokemon """
        return self.pkmn.heal(amount)
        
    def takeDamage(self, damage):
        """ Has the Pkmn take the given amount of damage """
        messages = []
        self.pkmn.takeDamage(damage)
        
        if self.pkmn.getCurrHP() == 0:
            messages = self.faint()
            
        return messages
        
    def faint(self):
        """ Makes the Pkmn faint """
        messages = []
        
        self.pkmn.setCurrHP(0)
        status, msg = StatusFactory.buildStatusFromAbbr("FNT")
        self.setStatus(status)
        
        messages.append(self.getHeader() + msg)
        return messages
        
    def fainted(self):
        """ Return whether the Wrapper's Pokemon is fainted """
        return self.pkmn.fainted()
        
    def getLevel(self):
        """ Returns the Wrapper's Pokemon's Level """
        return self.pkmn.level
        
    def getName(self):
        """ Returns the Wrapper's Pokemon's name """
        return self.pkmn.name
        
    def getRatioOfHealth(self, ratio, forDamage = False):
        """ Returns the given ratio of the Wrapper's Pokemon's Health """
        return self.pkmn.getRatioOfHealth(ratio, forDamage = forDamage)
        
    def getStat(self, stat):
        """ Returns the Wrapper's Pokemon's stat """
        return self.pkmn.getStat(stat)
        
    def setStat(self, stat, amount):
        """ Sets the Wrapper's Pokemon's Stat to the given amount """
        self.pkmn.setStat(stat, amount)
       
    def getCurrHP(self):
        """ Returns the Wrapper's Pokemon's Current HP """
        return self.pkmn.getCurrHP()
        
    def setCurrHP(self, amount):
        """ Sets the Wrapper's Pokemon's Current HP to the given amount """
        self.pkmn.setCurrHP(amount)
        
    def getStatus(self):
        """ Returns the Wrapper's Pokemon's Status """
        return self.pkmn.getStatus()
        
    def setStatus(self, status):
        """ Sets the Wrapper's Pokemon's Status """
        self.pkmn.setStatus(status)
        
    def getTypes(self):
        """ Returns the Wrapper's Pokemon's Types """
        return self.pkmn.getTypes()