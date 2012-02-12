import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.HitDelegates.hit_delegate import HitDelegate

class dodging(unittest.TestCase):
    """ Test that dodging returns the correct values """
    
    def setUp(self):
        """ Build Pkmn and Delegate for use in test cases """
        self.pkmn =  BuildPokemonBattleWrapper()
        self.delegate = HitDelegate(None, 100)
    
    def dodging(self):
        """ Test dodging function returns true correctly when the opp is dodging """
        self.pkmn.dodge = "DIG"
        assert self.delegate.dodging(self.pkmn), "Should be dodging"
        
    def notDodging(self):
        """ Test dodging function returns false when the opp is not dodging """
        self.pkmn.dodge = None
        assert not  self.delegate.dodging(self.pkmn), "Should not be dodging"
        
testcasesDodging= ["dodging", "notDodging"]
suiteDodging= unittest.TestSuite(map(dodging, testcasesDodging))

#########################################################
 
suites = [suiteDodging]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()