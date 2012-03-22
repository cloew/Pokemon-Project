
class NullDamageDelegate:
    """ Represents an attack that does No Damage """
    isNull = True
    
    def doDamage(self, user, target):
        return []