
class NullDamageDelegate:
    """ Represents an attack that does Zero Damage """
    isNull = True
    
    def doDamage(self, user, target):
        return 