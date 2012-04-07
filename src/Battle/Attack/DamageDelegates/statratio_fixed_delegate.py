from Battle.Attack.DamageDelegates.statratio_delegate import StatRatioDelegate

class StatRatioFixedDelegate(StatRatioDelegate):
    """ Represents an attack whose damage is based on a fixed set of power from the ratio of two stats """
    powerVariants = [60, 80, 120, 150]
        
    def getPower(self, user, target):
        """ Returns the power of the move based on the ratio of the stat """
        index = self.getIndex(user, target)
        return self.powerVariants[index]
        
    def getIndex(self, user, target):
        """ Returns the index for the Attack's power """
        ratio = self.getStatRatio(user, target)
        index = 3
        if ratio > 1/2.0:
            index = 0
        elif ratio > 1/3.0:
            index = 1
        elif ratio >1/4.0:
            index = 2
           
        return index