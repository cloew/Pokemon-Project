import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.recoil_delegate  import RecoilDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.pkmn = BuildPokemonBattleWrapper()
        
        self.ratio = 2
        self.damage = 50
        self.delegate = RecoilDelegate(self.ratio)
        
    def recoil(self):
        """ Test that recoil damage is done """
        self.pkmn.setCurrHP(self.damage)
        self.delegate.damage = self.damage
        self.delegate.applyEffect(self.pkmn, None)
        
        damageDone = self.damage - self.pkmn.getCurrHP()
        damage = self.damage/self.ratio
        assert damageDone == damage, "Should do damage  over ratio as damage"
        
    def message(self):
        """ Test that the message returned is correct """
        self.pkmn.setCurrHP(self.damage)
        self.delegate.damage = self.damage
        messages = self.delegate.applyEffect(self.pkmn, None)

        message = self.pkmn.getHeader() + RecoilDelegate.message
        assert len(messages) == 1, "Should get one message"
        assert messages[0] == message, "Message should be Pkmn's header and the Delegate's message"

# Collect all test cases in this class
testcasesApplyEffect = ["recoil", "message"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class normalize(unittest.TestCase):
    """ Tests that Normalize normalizes correctly """
    
    def setUp(self):
        """ Build the Recoil Delegate """
        self.delegate = RecoilDelegate(2)
        
    def zero(self):
        """ Test that < 1 is normalized correctly """
        damage = 0
        newDamage = self.delegate.normalize(damage)
        assert newDamage == 1, "Should return one if between 0 and 1"
        
    def normalize(self):
        """ Test that normalizing an int returns the int """
        damage = 3
        newDamage = self.delegate.normalize(damage)
        assert newDamage == damage, "Should return the number if its an int"

# Collect all test cases in this class      
testcasesNormalize = ["zero", "normalize",]
suiteNormalize  = unittest.TestSuite(map(normalize , testcasesNormalize ))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect, suiteNormalize]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()