import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildBattleAction, BuildAttackAction, BuildActionLock

from Battle.Attack.EffectDelegates.encore_delegate import EncoreDelegate

class applyEffect(unittest.TestCase):
    """ Test cases of applyEffect """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.pkmn = BuildPokemonBattleWrapper()
        self.turns = 3
        self.action = BuildAttackAction()
        self.delegate = EncoreDelegate(self.turns, 1)
        
    def immune(self):
        """ Test that the encore is not applied when the Pkmn is immune """
        self.pkmn.lastAction = None
        self.pkmn.encore = None
        
        messages = self.delegate.applyEffect(self.pkmn, None)
        assert len(messages) == 0, "Should get no messages"
        assert self.pkmn.encore is None, "Should not have an encore effect"
        
    def notImmune(self):
        """ Test that the encore is applied when the Pkmn is not immune """
        self.pkmn.lastAction = self.action
        self.pkmn.encore = None
        
        messages = self.delegate.applyEffect(self.pkmn, None)
        assert len(messages) == 0, "Should get no messages"
        
        encore = self.pkmn.encore
        assert encore, "Should have an encore effect"
        assert encore.parent == self.pkmn, "Should belong to the Pkmn"
        assert encore.action is self.action, "Should be the last action"
        assert encore.turnsToGo == self.turns, "Should last the turn count of the delegate"

# Collect all test cases in this class
testcasesApplyEffect = ["immune", "notImmune"]
suiteApplyEffect = unittest.TestSuite(map(applyEffect, testcasesApplyEffect))

##########################################################

class immune(unittest.TestCase):
    """ Test cases of immune """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.pkmn = BuildPokemonBattleWrapper()
        self.delegate = EncoreDelegate(3, 1)
        
    def noAction(self):
        """ Test that the target is immune when it doesn't have a last action """
        self.pkmn.lastAction = None
        self.pkmn.encore = None
        
        immune = self.delegate.immune(self.pkmn)
        assert immune, "Pkmn should be immune when no action"
        
    def battleAction(self):
        """ Test that the target is immune when it doesn't have a attack action """
        self.pkmn.lastAction = BuildBattleAction()
        self.pkmn.encore = None
        
        immune = self.delegate.immune(self.pkmn)
        assert immune, "Pkmn should be immune when action isn't an attack"
        
    def hasEncore(self):
        """ Test that the target is immune when it has an encore """
        self.pkmn.lastAction = BuildAttackAction()
        self.pkmn.encore = BuildActionLock()
        
        immune = self.delegate.immune(self.pkmn)
        assert immune, "Pkmn should be immune when you have an encore"
        
    def notImmune(self):
        """ Test that the target is not immune when it has an attack action """
        self.pkmn.lastAction = BuildAttackAction()
        self.pkmn.encore = None
        
        immune = self.delegate.immune(self.pkmn)
        assert not immune, "Pkmn should not be immune when has an attack action & no encore"

# Collect all test cases in this class
testcasesImmune = ["noAction", "battleAction", "hasEncore", "notImmune"]
suiteImmune = unittest.TestSuite(map(immune, testcasesImmune))

##########################################################

# Collect all test cases in this file
suites = [suiteApplyEffect, suiteImmune]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()