from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.statratio_fixed_delegate import StatRatioFixedDelegate

import unittest

class getPower(unittest.TestCase):
    """ Test that core damage is calculated correctly """ 
    
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.userPkmn = self.user.pkmn
        self.targetPkmn = self.target.pkmn
        
        self.stat = "SPD"
        self.delegate = StatRatioFixedDelegate(None, 1, self.stat)
        self.lvl = 50


# Collect all test cases in this class      
testcasesGetPower = []
suiteGetPower = unittest.TestSuite(map(getPower, testcasesGetPower))

#########################################################

suites = [suiteGetPower]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()