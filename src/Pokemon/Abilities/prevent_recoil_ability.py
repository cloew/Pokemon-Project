from ability import Ability

class PreventRecoilAbility(Ability):
    """ Represents an ability that prevents recoil """
    
    def preventRecoil(self):
        """ Return if recoil damage is prevented """
        return True