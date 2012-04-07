from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.statratio_delegate import StatRatioDelegate

import unittest

class getStatRatio(unittest.TestCase):
    """ Test that the ratio is calculated properly """ 
    
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.userPkmn = self.user.pkmn
        self.targetPkmn = self.target.pkmn
        
        self.stat = "SPD"
        self.delegate = StatRatioDelegate(None, 1, self.stat)
        self.lvl = 50
        
    def equalRatio(self):
        """ Test that the ratio is 1 """
        self.userPkmn.battleDelegate.stats[self.stat] = self.lvl
        self.targetPkmn.battleDelegate.stats[self.stat] = self.lvl
        ratio = self.delegate.getStatRatio(self.user, self.target)
        
        assert ratio == 1, "Ratio should be 1"
        
    def doubleRatio(self):
        """ Test that the ratio is 2 """
        self.userPkmn.battleDelegate.stats[self.stat] = self.lvl
        self.targetPkmn.battleDelegate.stats[self.stat] = self.lvl*2
        ratio = self.delegate.getStatRatio(self.user, self.target)
        
        assert ratio == 2, "Ratio should be 2"
        
    def halfRatio(self):
        """ Test that the ratio is 1/2 """
        self.userPkmn.battleDelegate.stats[self.stat] = self.lvl*2
        self.targetPkmn.battleDelegate.stats[self.stat] = self.lvl
        ratio = self.delegate.getStatRatio(self.user, self.target)
        
        assert ratio == 1/2.0, "Ratio should be 1/2"

# Collect all test cases in this class      
testcasesGetStatRatio = ["equalRatio", "doubleRatio", "halfRatio"]
suiteGetStatRatio = unittest.TestSuite(map(getStatRatio, testcasesGetStatRatio))

#########################################################

suites = [suiteGetStatRatio]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()