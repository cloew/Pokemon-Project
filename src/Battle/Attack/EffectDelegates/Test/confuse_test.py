import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.confuse_delegate import ConfuseDelegate
from Battle.SecondaryEffects.confusion import Confusion

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        self.delegate = ConfuseDelegate(1)
        
    def alreadyConfused(self):
        """ Test that confusion is not applied when the target is already confused """
        self.user.secondaryEffects = [Confusion()]
        message = self.user.getHeader() + Confusion.already
        messages = self.delegate.applyEffect(self.user, self.target)
        
        assert len(messages) == 1, "Should get one message"
        assert messages[0]  == message, "Should say that the Pkmn is already confused"
        
        assert len(self.user.secondaryEffects) == 1, "Pkmn should not get another confusion effect"
        
    def notConfused(self):
        """ Test that confusion is applied when the target is not confused """
        self.user.secondaryEffects = []
        message = self.user.getHeader() + Confusion.start
        messages = self.delegate.applyEffect(self.user, self.target)
        
        assert len(messages) == 1, "Should get one message"
        assert messages[0]  == message, "Should say that the Pkmn is now confused"
        
        assert len(self.user.secondaryEffects) == 1, "Pkmn should get a confusion effect"
        assert self.delegate.isConfused(self.user), "The Pkmn should now be confused"
        
    

# Collect all test cases in this class
testcasesApplyEffect = ["alreadyConfused", "notConfused"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class isConfused(unittest.TestCase):
    """ Test cases of isConfused """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.pkmn = BuildPokemonBattleWrapper()
        self.delegate = ConfuseDelegate(1)
        
    def alreadyConfused(self):
        """ Test that isConfused returns correctly when the pkmn is Confused """
        self.pkmn.secondaryEffects = [Confusion()]
        confused = self.delegate.isConfused(self.pkmn)
        assert confused, "Pokemon should be confused if it has a Confusion Effect"
        
        
    def notConfused(self):
        """ Test that isConfused returns correctly when the pkmn is not Confused """
        self.pkmn.secondaryEffects = []
        confused = self.delegate.isConfused(self.pkmn)
        assert not confused, "Pokemon should not be confused if it has no Confusion Effect"

# Collect all test cases in this class
testcasesIsConfused = ["alreadyConfused", "notConfused"]
suiteIsConfused = unittest.TestSuite(map(isConfused, testcasesIsConfused))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect, suiteIsConfused]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()