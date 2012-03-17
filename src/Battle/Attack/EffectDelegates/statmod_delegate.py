from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate

class StatModDelegate(EffectDelegate):
    """ Handles modifying stats """
    
    max = 6
    min = -6
    
    noChangeDown = " cannot be lowered anymore"
    noChangeUp = " cannot be raised anymore"
    riseOrFall = {True:"rose", False:"fell"}
    sharply = {1:".", 2:" sharply.", 12:" as much as it could."}
    
    def __init__(self, stat, degree, side):
        """ Builds a StatModDelegate """
        self.stat = stat
        self.degree = degree
        self.affectUser = side
    
    def applyEffect(self, user, target):
        """ Applies the Deleagates effect """
        pkmn = self.getEffectedPokemon(user, target)
        return self.applyMod(pkmn)
            
    def applyMod(self, pkmn):
        """ Apply the modifier to the given pkmn """
        degree, abilityMessages = pkmn.getAbility().\
                                                onStatMod(pkmn, self.stat, self.degree, self.affectUser)
                                                
        noChange, messages = self.checkNoChange(pkmn, degree, abilityMessages)
        if noChange:
            return messages
            
        return self.changeStats(pkmn, degree)
        
    def checkNoChange(self, pkmn, degree, abilityMessages):
        """ Check if anything will change """
        noChange = False
        messages = []
        header = self.getHeader(pkmn)
        
        if degree == 0:
            noChange = True
            messages = abilityMessages
        elif degree > 0 and pkmn.statMods[self.stat] == self.max:
            noChange = True
            messages = [header + StatModDelegate.noChangeUp]
        elif degree < 0 and pkmn.statMods[self.stat] == self.min:
            noChange = True
            messages = [header + StatModDelegate.noChangeDown]
            
        return noChange, messages
        
    def changeStats(self, pkmn, degree):
        """ Actually change the pkmn's stat mod """
        messages = [self.getHeader(pkmn) + self.getMessage()] 
        newMod = pkmn.statMods[self.stat] + degree
        
        if newMod > self.max:
            pkmn.statMods[self.stat] = self.max
        elif newMod < self.min:
            pkmn.statMods[self.stat] = self.min
        else:
            pkmn.statMods[self.stat] = newMod
        
        return messages       
        
    def getMessage(self):
        """ Return the appropriate message for whether the stat increased or decreased """
        message = StatModDelegate.riseOrFall[self.degree>0] 
        return message + StatModDelegate.sharply[abs(self.degree)]
        
    def getHeader(self, pkmn):
        """ Returns the Pokemon and stat as a string """
        return "{0}'s {1} ".format(pkmn.getHeader(), self.stat)