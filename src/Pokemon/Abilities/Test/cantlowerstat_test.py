from Pokemon.Abilities.cantlowerstat_ability import CantLowerStatAbility

from Battle.battle_side import BattleSide
from Battle.Status.status import Status
from Battle.Status.paralysis import Paralysis
from Pokemon.pokemon import Pokemon
from Trainer.trainer import Trainer

import unittest

class onStatMod(unittest.TestCase):
    """ Test that onStatMod operates correctly """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        
        self.stat = "ATK"
        self.stat2 = "DEF"
        
        self.degree = -1
        self.degree2 = 1
        
        self.ability = CantLowerStatAbility("", self.stat)
        
    def statChange_notStat(self):
        """ Check gaurded stat is the only protected stat """
        degree, messages = self.ability.onStatMod(self.side, self.stat2, self.degree, 0)
        
        assert degree == self.degree, "Degree should not be altered when stat lowered is not protected."
        assert len(messages) == 0, "Messages be empty."
        
    def statChange_Raised(self):
        """ Check that the stat is only protected against lowering """
        degree, messages = self.ability.onStatMod(self.side, self.stat, self.degree2, 0)
        
        assert degree == self.degree2, "Degree should not be altered when stat is raised."
        assert len(messages) == 0, "Messages be empty."
        
    def statChange_SelfInflicted(self):
        """ Check that the stat is only protected against opp """
        degree, messages = self.ability.onStatMod(self.side, self.stat, self.degree, 1)
        
        assert degree == self.degree, "Degree should not be altered when self-inflicted."
        assert len(messages) == 0, "Messages be empty."
        
    def blockStatChange(self):
        """ Check that the stat decrease is blocked """
        degree, messages = self.ability.onStatMod(self.side, self.stat, self.degree, 0)
        
        assert degree == 0, "Degree should be zero."
        assert len(messages) == 1, "Should have a message."
        
testcasesOnStatMod = ["statChange_notStat", "statChange_Raised", "statChange_SelfInflicted", "blockStatChange"]
suiteOnStatMod = unittest.TestSuite(map(onStatMod, testcasesOnStatMod))

##########################################################

 
suites = [suiteOnStatMod]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()