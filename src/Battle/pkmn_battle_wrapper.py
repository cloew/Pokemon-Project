from Battle.Status.statusfactory import StatusFactory
from Pokemon.pokemon_factory import PokemonFactory

class PkmnBattleWrapper:
    """ Represents one Pkmn's slot in a battle """
    
    def __init__(self, side):
        """ Build the Pkmn Wrapper """
        self.side = side
        self.pkmn = None
        self.original = None # The original Pkmn from the Trainer's belt, kept so the Trainer is aware of exactly how the Pkmn is
        #self.trainer = trainer # May add back later if I decide to have mulitple trainers on the same side in a battle
        
        self.statMods = {"ATK":0, "DEF":0, "SPD":0, "SATK":0, "SDEF":0, 
                                "ACC":0, "EVAS":0, "CRT":0}
        self.reset()
        
    def sendOutPkmn(self, pkmn, reset = True):
        """ Sends out the wrapper's pkmn """
        if reset:
            self.reset()
            
        self.lastAction = None
        self.setPkmn(pkmn)
        return [self.side.trainer.announcePkmn(pkmn)]
        
    def reset(self):
        self.resetStatMods()
        
        self.flinching = False
        self.encore = 0
        
        self.lastAction = None
        self.actionLock = None
        self.dodge = None
        
        self.secondaryEffects = []
        
    def resetStatMods(self):
        """ Resets the stat mods for the side """
        for key in self.statMods:
            self.statMods[key] = 0
            
    def afterTurn(self):
        """ Perform affects of items/status/field hazards after the acting side performs its turn """
        messages = []
        messages += self.getAbility().attemptAfterTurn(self)
        messages += self.getStatus().attemptAfterTurn(self)
        
        for effect in  self.secondaryEffects:
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
        
    def setAbility(self, ability):
        """ Sets the Wrapper's Pokemon's Ability """
        self.pkmn.ability = ability
        
    def getAttacks(self):
        """ Returns the Wrapper's Pokemon's Attacks """
        return self.pkmn.getAttacks()
        
    def heal(self, amount):
        """ Heal the Wrapper's Pokemon """
        self.original.heal(amount)
        return self.pkmn.heal(amount)
        
    def takeDamage(self, damage):
        """ Has the Pkmn take the given amount of damage """
        messages = []
        self.original.takeDamage(damage)
        self.pkmn.takeDamage(damage)
        
        if self.pkmn.getCurrHP() == 0:
            messages = self.faint()
            
        return messages
        
    def faint(self):
        """ Makes the Pkmn faint """
        messages = []
        
        self.setCurrHP(0)
        status, msg = StatusFactory.buildStatusFromAbbr("FNT")
        self.setStatus(status)
        
        messages.append(self.getHeader() + msg)
        return messages
        
    def fainted(self):
        """ Return whether the Wrapper's Pokemon is fainted """
        return self.pkmn.fainted()
        
    def setPkmn(self, pkmn):
        """ Set the PkmnBattleWrapper's Pokemon """
        self.original = pkmn
        self.pkmn = PokemonFactory.copy(pkmn)
        
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
        self.original.setCurrHP(amount)
        self.pkmn.setCurrHP(amount)
        
    def getStatus(self):
        """ Returns the Wrapper's Pokemon's Status """
        return self.pkmn.getStatus()
        
    def setStatus(self, status):
        """ Sets the Wrapper's Pokemon's Status """
        self.original.setStatus(status)
        self.pkmn.setStatus(status)
        
    def hasStatus(self):
        """  Returns if the pkmn has a status """
        return not self.getStatus().abbr  == "   "
        
    def getTypes(self):
        """ Returns the Wrapper's Pokemon's Types """
        return self.pkmn.getTypes()