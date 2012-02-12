import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.HitDelegates.piercedodge_delegate import PierceDodgeDelegate

class dodging(unittest.TestCase):
    """ Test that dodging returns the correct values """
    
    def setUp(self):
        """ Build Pkmn and Delegate for use in test cases """
        self.pkmn =  BuildPokemonBattleWrapper()
        self.pierce = "DIG"
        self.delegate = PierceDodgeDelegate(None, 100, self.pierce)
    
    def dodging(self):
        """ Test dodging function returns true correctly when the opp is dodging """
        self.pkmn.dodge = "FLY"
        assert self.delegate.dodging(self.pkmn), "Should be dodging"
        
    def notDodging(self):
        """ Test dodging function returns false when the opp is not dodging """
        self.pkmn.dodge = None
        assert not  self.delegate.dodging(self.pkmn), "Should not be dodging"
        
    def piercing(self):
        """ Test dodging function returns true correctly when piercing the opps dodge """
        self.pkmn.dodge = self.pierce
        assert not  self.delegate.dodging(self.pkmn), \
                "Should be dodging, but the user should pierce"
        
testcasesDodging= ["dodging", "notDodging", "piercing"]
suiteDodging= unittest.TestSuite(map(dodging, testcasesDodging))

#########################################################
 
suites = [suiteDodging]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()