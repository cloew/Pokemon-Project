import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Status.poison import Poison
from Battle.Status.toxic_poison import ToxicPoison

class init(unittest.TestCase):
    """ Test that init initializes correctly """
    
    def setUp(self):
        """ Builds the ToxicPoison status"""
        self.status = ToxicPoison()
    
    def builtRight(self):
        """ Test if the init function initializes the object correctly """
        assert self.status.abbr == Poison.abbr, "Abbr should be same as Poison's"
        assert self.status.counter == 1, "Counter should be 1"
        
testcasesInit = ["builtRight"]
suiteInit = unittest.TestSuite(map(init, testcasesInit))

##########################################################

class afterTurn(unittest.TestCase):
    """ Test that after Turn acts correctly """
    
    def setUp(self):
        """ Builds the ToxicPoison status"""
        self.status = ToxicPoison()
        self.pkmn = BuildPokemonBattleWrapper()
    
    def counterIsUpped(self):
        """ Test if the counter is increased """
        self.status.counter = 1
        self.status.afterTurn(self.pkmn)
        
        assert self.status.counter == 2, "Counter should be 2"
        
testcasesAfterTurn = ["counterIsUpped",]
suiteAfterTurn = unittest.TestSuite(map(afterTurn, testcasesAfterTurn))

##########################################################

class getDamage(unittest.TestCase):
    """ Test that immune returns correctly """
    
    def setUp(self):
        """ Builds the ToxicPoison status"""
        self.status = ToxicPoison()
        self.pkmn = BuildPokemonBattleWrapper() #Pokemon("BULBASAUR")
        self.hp = 64.0
        self.pkmn.setStat("HP", self.hp)
    
    def damage1stTurn(self):
        """ Test if 1st turn damage is correct"""
        self.status.counter = 1
        damage = self.status.getDamage(self.pkmn)
        
        assert damage == self.hp/ToxicPoison.ratio, "Damage should be hp/ratio"
            
    def damage2ndTurn(self):
        """ Test if it can correctly identify when the target is immune """
        self.status.counter = 2
        damage = self.status.getDamage(self.pkmn)
        
        assert damage == 2*self.hp/ToxicPoison.ratio, "Damage should be double hp/ratio"
        
testcasesGetDamage = ["damage1stTurn", "damage2ndTurn"]
suiteGetDamage = unittest.TestSuite(map(getDamage, testcasesGetDamage))

##########################################################
 
suites = [suiteInit, suiteAfterTurn, suiteGetDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()