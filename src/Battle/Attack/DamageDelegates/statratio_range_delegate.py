from Battle.Attack.DamageDelegates.statratio_delegate import StatRatioDelegate

class StatRatioRangeDelegate(StatRatioDelegate):
    """ Represents an attack whose damage is based on a range from the ratio of two stats """
    max = 150
    base = 25
        
    def getPower(self, user, target):
        """ Returns the power of the move based on the ratio of the stat """
        ratio = self.getStatRatio(user, target)
        power = self.base*ratio
        if power > self.max:
            power = self.max
        return power