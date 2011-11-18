
class StatModDelegate(object):
    """ Handles modifying stats """
    
    noChangeDown = " cannot be lowered anymore"
    noChangeUp = " cannot be raised anymore"
    riseOrFall = {True:"rose", False:"fell"}
    sharply = {1:".", 2:" sharply.",}
    
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
        header = self.getHeader(side)
        messages = [header + self.getMessage()] 
        
        degree, abilityMessages = side.currPokemon.ability.\
                                                onStatMod(side, self.stat, self.degree, self.affectUser)
        
        newMod = side.statMods[self.stat] + degree
        
        if degree == 0:
            messages = abilityMessages
        elif newMod > 6:
            side.statMods[self.stat] = 6
            messages = [header + StatModDelegate.noChangeUp]
        elif newMod < -6:
            side.statMods[self.stat] = -6
            messages = [header + StatModDelegate.noChangeDown]
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
        
        