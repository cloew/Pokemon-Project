import unittest
from Test.test_helper import BuildPokemon

class isFainted(unittest.TestCase):
    """ Tests logic for determining if a Pokemon is fainted or not """
    
    def  setUp(self):
        """ Build the Pokemon for use in the tests """
        self.pkmn = BuildPokemon()
        
    def isNotFainted(self):
        """ Test a Pokemon with health is not fainted """
        self.pkmn.battleDelegate.currHP = 1
        assert not self.pkmn.fainted(), "A Pokemon with HP > 0 should not be fainted"
        
    def isFainted(self):
        """ Test a Pokemon is fainted when it has no health """
        self.pkmn.battleDelegate.currHP = 0
        assert self.pkmn.fainted(), "A Pokemon with 0 HP should be fainted"

# Collect all test cases in this file
testcasesIsFainted = ["isNotFainted", "isFainted"]
suiteIsFainted= unittest.TestSuite(map(isFainted, testcasesIsFainted))

##########################################################
    
class getRatioOfHealth(unittest.TestCase):
    """ Tests getRatio returns the correct amount of the HP """
    
    def  setUp(self):
        """ Build the Pokemon for use in the test """
        self.pkmn = BuildPokemon()
        self.ratio = 2
        self.hp1 = 50
        self.hp2 = 51
        self.hp3 = 10
        self.hp4 = 1
        self.half = 25
        
    def setHP(self, pkmn, amount):
        """ Sets the HP and currHP of the given Pkmn """
        pkmn.setStat("HP", amount)
        pkmn.setCurrHP(amount)
        
    def getRatio(self):
        """ Test ratio with no truncation"""
        self.setHP(self.pkmn, self.hp1)
        ratio = self.pkmn.getRatioOfHealth(self.ratio)
        ratioForDamage = self.pkmn.getRatioOfHealth(self.ratio, forDamage = True)
        
        assert ratio == self.half, "getRatio result should be hp/ratio"
        assert ratioForDamage == self.half, "getRatio for Damage result should be hp/ratio"
        
    def getRatioTruncated(self):
        """ Test ratio with truncation """
        self.setHP(self.pkmn, self.hp2)
        ratio = self.pkmn.getRatioOfHealth(self.ratio)
        ratioForDamage = self.pkmn.getRatioOfHealth(self.ratio, forDamage = True)
        
        assert ratio == self.half, "getRatio result should be hp/ratio truncated"
        assert ratioForDamage == self.half, "getRatio for Damage result should be hp/ratio"
        
    def getRatioUnderCurrHP(self):
        """ Test ratio returned is equivalent to the Curr HP when CurrHP Is less than """
        self.pkmn.setStat("HP", self.hp1)
        self.pkmn.setCurrHP(self.hp3)
        ratio = self.pkmn.getRatioOfHealth(self.ratio)
        ratioForDamage = self.pkmn.getRatioOfHealth(self.ratio, forDamage = True)
        
        assert ratio == self.half, "getRatio result should be Current HP"
        assert ratioForDamage == self.hp3, "getRatio for Damage result should be hp/ratio"
        
    def getRatioUnder1(self):
        """ Test ratio with result under 1 """
        self.setHP(self.pkmn, self.hp4)
        ratio = self.pkmn.getRatioOfHealth(self.ratio)
        ratioForDamage = self.pkmn.getRatioOfHealth(self.ratio, forDamage = True)
        
        assert ratio == 1, "getRatio result should be 1 if hp/ratio would be under 1"
        assert ratioForDamage == 1, "getRatio for Damage result should be 1 if hp/ratio would be under 1"

# Collect all test cases in this file
testcasesGetRatioOfHealth = ["getRatio", "getRatioTruncated", "getRatioUnderCurrHP", "getRatioUnder1"]
suiteGetRatioOfHealth = unittest.TestSuite(map(getRatioOfHealth, testcasesGetRatioOfHealth))

##########################################################
    
suites = [suiteIsFainted, suiteGetRatioOfHealth]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()