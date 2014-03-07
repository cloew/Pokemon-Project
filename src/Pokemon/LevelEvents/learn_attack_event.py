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
        
    def learnAndReplace(self, attack):
        """ Learn the new attack and Replace the given attack """
        attacks = self.pokemon.getAttacks()
        index = attacks.index(attack)
        attacks[index] = self.attack
        
        forgotMessage = "{0} forgot {1}...".format(self.pokemon.name, attack.name)
        learnedMessage = "And {0} learned {1}".format(self.pokemon.name, self.attack.name)
        return [forgotMessage, learnedMessage]
        
    def getTryToLearnMessages(self):
        """ Return the messages for the Pokemon to try to learn an attack """
        messages = []
        messages.append("{0} is trying to learn {1}.".format(self.pokemon.name, self.attack.name))
        messages.append("But {0} can't learn more than four moves.".format(self.pokemon.name))
        messages.append("Forget a move to learn {0}?".format(self.attack.name))
        return messages
        
    def getStopLearningMessage(self):
        """ Return the Stop Learning Message """
        return "Stop trying to learn {0}".format(self.attack.name)