from Pokemon.Abilities.ability import Ability

class EffectivenessAbility(Ability):
    """ An Ability with modified effectivensses """
    
    def __init__(self, differentEffectivenesses):
        """  """
        Ability.__init__(self)
        
        for attackType in differentEffectivensses:
            for type in differentEffectivenesses[attackType]:
                if attackType in self.effectivenessTable:
                    if type in self.effectivenessTable[attackType]:
                        self.effectivenessTable[attackType][type] = differentEffectivenesses[attackType][type]