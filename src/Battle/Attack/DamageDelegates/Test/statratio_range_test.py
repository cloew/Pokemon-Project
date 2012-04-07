from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.statratio_range_delegate import StatRatioRangeDelegate

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
        self.delegate = StatRatioRangeDelegate(None, 1, self.stat)
        self.lvl = 50
        
    def basePower(self):
        """ Test that the base power is correct """
        self.userPkmn.battleDelegate.stats[self.stat] = 25
        self.targetPkmn.battleDelegate.stats[self.stat] = 25
        power = self.delegate.getPower(self.user, self.target)
        
        assert power == StatRatioRangeDelegate.base, "Power should be the base when the ratio of the stat is 0"
        
    def powerIsLarger(self):
        """ Test that the power is greater when the user's stat is lower """
        self.userPkmn.battleDelegate.stats[self.stat] = 20
        self.targetPkmn.battleDelegate.stats[self.stat] = 25
        power = self.delegate.getPower(self.user, self.target)
        
        assert power > StatRatioRangeDelegate.base, "Power should be larger when user's stat decreases"
        
    def powerIsSmaller(self):
        """ Test that the power is smaller when the user's stat is higher """
        self.userPkmn.battleDelegate.stats[self.stat] = 30
        self.targetPkmn.battleDelegate.stats[self.stat] = 25
        power = self.delegate.getPower(self.user, self.target)
        
        assert power < StatRatioRangeDelegate.base, "Power should be smaller when user's stat increases"
        
    def powerIsMax(self):
        """ Test that the power is not greater than the max """
        self.userPkmn.battleDelegate.stats[self.stat] = 1
        self.targetPkmn.battleDelegate.stats[self.stat] = 300
        power = self.delegate.getPower(self.user, self.target)
        
        assert power ==  StatRatioRangeDelegate.max, "Power should be max at greatest"


# Collect all test cases in this class      
testcasesGetPower = ["basePower", "powerIsLarger", "powerIsSmaller", "powerIsMax"]
suiteGetPower = unittest.TestSuite(map(getPower, testcasesGetPower))

#########################################################

suites = [suiteGetPower]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()