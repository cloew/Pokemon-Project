import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Status.burn import Burn

class afterTurn(unittest.TestCase):
    """ Test that afterTurn works correctly """
    
    def setUp(self):
        """ Builds the Paralysis status"""
        self.status = Burn()
        self.pkmn = BuildPokemonBattleWrapper()
        
    def damage(self):
        """ Test that the damage is done correctly """
        self.pkmn.setStat("HP", 32)
        self.pkmn.setCurrHP(32)
        self.status.afterTurn(self.pkmn)
        damage = self.pkmn.getStat("HP") - self.pkmn.getCurrHP()
        assert damage == self.pkmn.getRatioOfHealth(Burn.ratio), "Damage should be Burn Ratio of Health"
    
    def message(self):
        """ Test that the message is returned correctly """
        messages = self.status.afterTurn(self.pkmn)
        message = self.pkmn.getHeader() + Burn.intermittent
        assert len(messages) == 1, "Should get one message"
        assert messages[0] == message, "Message should be that the Pkmn was damaged by the Burn"
    
        
testcasesAfterTurn = ["damage", "message"]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class getStatMod(unittest.TestCase):
    """ Test that statMod returns the correct values for all stats """
    
    def setUp(self):
        """ Builds the Paralysis status"""
        self.status = Burn()
    
    def checkStatMods(self):
        """ Test that stat modifiers are correct for Burn
        .5 for ATK, 1 for the rest """
        for key in self.status.statMods:
            if key == "ATK":
                assert self.status.getStatMod(key) == .5, "ATK should be .5"
            else:
                assert self.status.getStatMod(key) == 1, "All stats, except ATK, should be 1"
        
    
        
testcasesGetStatMod = ["checkStatMods"]
suiteGetStatMod = unittest.TestSuite(map(getStatMod, testcasesGetStatMod))

##########################################################

class immune(unittest.TestCase):
    """ Test that immune returns correctly """
    
    def setUp(self):
        """ Builds the Paralysis status"""
        self.status = Burn()
    
    def immune(self):
        """ Test if it can correctly identify when the target is immune """
        types = ["FIRE"]
        other = "ELECTRIC"
        assert self.status.immune(types, other), "Should be immune if FIRE"
        
        types = ["GROUND", "FIRE"]
        other = "ELECTRIC"
        assert self.status.immune(types, other), "Should be immune if FIRE regardless of other type"
            
    def notImmune(self):
        """ Test if it can correctly identify when the target is immune """
        types = ["ELECTRIC"]
        other = "FIRE"
        assert not self.status.immune(types, other), "Should not be immune if not FIRE"
        
testcasesImmune = ["immune", "notImmune"]
suiteImmune= unittest.TestSuite(map(immune, testcasesImmune))

##########################################################
 
suites = [suiteAfterTurn, suiteGetStatMod, suiteImmune]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()