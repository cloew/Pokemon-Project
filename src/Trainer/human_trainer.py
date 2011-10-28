from Battle.Actions.attack_action import AttackAction
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import random

class HumanTrainer(Trainer):
    """ Represents a Pokemon Trainer """
    header = ""
    def getHeader(self):
        """ Return the header based on the type of trainer """
        return HumanTrainer.header