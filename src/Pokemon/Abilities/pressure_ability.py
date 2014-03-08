from ability import Ability

class PressureAbility(Ability):
    """ Represents the Pressure Ability """
    
    def powerPointsPressure(self):
        """ Return the power point Pressure this Pokemon applies """
        return 2
        
    def onEntry(self):
        """ Perform when a Pkmn arrives in the battle """
        return ["{0} is exerting its Pressure."]