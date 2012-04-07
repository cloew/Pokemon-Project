from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.statratio_fixed_delegate import StatRatioFixedDelegate

import unittest

class getIndex(unittest.TestCase):
    """ Test that the correct index is returned """ 
    
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.userPkmn = self.user.pkmn
        self.targetPkmn = self.target.pkmn
        
        self.stat = "SPD"
        self.delegate = StatRatioFixedDelegate(None, 1, self.stat)
        self.lvl = 50
        
    def overHalf(self):
        """ Test the power is corretc when the ratio is over 1/2 """
        self.userPkmn.battleDelegate.stats[self.stat] = self.lvl*2
        self.targetPkmn.battleDelegate.stats[self.stat] = self.lvl+1
        index = self.delegate.getIndex(self.user, self.target)
        
        assert index == 0, "Index should be 0"
        
    def overThird(self):
        """ Test the power is correct when the ratio is over 1/3 """
        self.userPkmn.battleDelegate.stats[self.stat] = self.lvl*3
        self.targetPkmn.battleDelegate.stats[self.stat] = self.lvl+1
        index = self.delegate.getIndex(self.user, self.target)
        
        assert index == 1, "Index should be 1"
        
    def overFourth(self):
        """ Test the power is correct when the ratio is over 1/4 """
        self.userPkmn.battleDelegate.stats[self.stat] = self.lvl*4
        self.targetPkmn.battleDelegate.stats[self.stat] = self.lvl+1
        index = self.delegate.getIndex(self.user, self.target)
        
        assert index == 2, "Index should be 2"
        
    def otherwise(self):
        """ Test the power is correct when the ratio is under or equal to 1/4 """
        self.userPkmn.battleDelegate.stats[self.stat] = self.lvl*4
        self.targetPkmn.battleDelegate.stats[self.stat] = self.lvl
        index = self.delegate.getIndex(self.user, self.target)
        
        assert index == 3, "Index should be 3"


# Collect all test cases in this class      
testcasesGetIndex = ["overHalf", "overThird", "overFourth", "otherwise"]
suiteGetIndex = unittest.TestSuite(map(getIndex, testcasesGetIndex))

#########################################################

suites = [suiteGetIndex]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()