
class StatModDelegate(object):
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
    
    def applyEffect(self, actingSide, otherSide):
        """ Applies the Deleagates effect """
        if self.affectUser:
            return self.applyMod(actingSide)
        else:
            return self.applyMod(otherSide)
            
    def applyMod(self, side):
        """ Apply the modifier to the given side """
        degree, abilityMessages = side.currPokemon.ability.\
                                                onStatMod(side, self.stat, self.degree, self.affectUser)
                                                
        noChange, messages = self.checkNoChange(side, degree, abilityMessages)
        if noChange:
            return messages
            
        return self.changeStats(side, degree)
        
    def checkNoChange(self, side, degree, abilityMessages):
        """ Check if anything will change """
        noChange = False
        messages = []
        header = self.getHeader(side)
        
        if degree == 0:
            noChange = True
            messages = abilityMessages
        elif degree > 0 and side.statMods[self.stat] == self.max:
            noChange = True
            messages = [header + StatModDelegate.noChangeUp]
        elif degree < 0 and side.statMods[self.stat] == self.min:
            noChange = True
            messages = [header + StatModDelegate.noChangeDown]
            
        return noChange, messages
        
    def changeStats(self, side, degree):
        """ Actually change the side's stat mod """
        messages = [self.getHeader(side) + self.getMessage()] 
        newMod = side.statMods[self.stat] + degree
        
        if newMod > self.max:
            side.statMods[self.stat] = self.max
        elif newMod < self.min:
            side.statMods[self.stat] = self.min
        else:
            side.statMods[self.stat] = newMod
        
        return messages       
        
    def getMessage(self):
        """ Return the appropriate message for whether the stat increased or decreased """
        message = StatModDelegate.riseOrFall[self.degree>0] 
        return message + StatModDelegate.sharply[abs(self.degree)]
        
    def getHeader(self, side):
        """ Returns the Pokemon and stat as a string """
        return "{0}'s {1} ".format(side.getHeader(), self.stat)