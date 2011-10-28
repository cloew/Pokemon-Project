from Battle.Attack.HitDelegates.hit_delegate import HitDelegate
from Battle.battle_side import BattleSide
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon

import unittest

class dodging(unittest.TestCase):
    """ Test that dodging returns the correct values """
    def setUp(self):
        """ Build side for use in test cases """
        trainer = Trainer()
        pokemon = Pokemon("BULBASAUR")
        trainer.beltPokemon = [pokemon]
        self.side = BattleSide(trainer)
        self.delegate = HitDelegate(None, 100, "")
    
    def dodging(self):
        """ Test dodging function returns true correctly when the opp is dodging """
        self.side.dodge = "DIG"
        assert self.delegate.dodging(self.side), "Opp side should be dodging"
        
    def notDodging(self):
        """ Test dodging function returns false when the opp is not dodging """
        self.side.dodge = None
        assert not  self.delegate.dodging(self.side), "Opp side should not be dodging"
        
testcasesDodging= ["dodging", "notDodging"]
suiteDodging= unittest.TestSuite(map(dodging, testcasesDodging))

#########################################################
 
suites = [suiteDodging]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()