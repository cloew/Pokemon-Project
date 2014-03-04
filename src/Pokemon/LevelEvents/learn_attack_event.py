from level_event import LevelEvent

class LearnAttackEvent(LevelEvent):
    """ Represents the event to learn a Pokemon Attack """
    
    def __init__(self, pokemon, attack):
        """ Initialize the Learn Attack Event """
        self.attack = attack
        LevelEvent.__init__(self, pokemon)
        
    def canLearnAttack(self):
        """ Return if the Pokemon can learn the attack """
        return len(self.pokemon.getAttacks()) < 4
        
    def perform(self):
        """ Perform the event """
        self.pokemon.getAttacks().append(self.attack)
        return ["{0} learned {1}.".format(self.pokemon.name, self.attack.name)]