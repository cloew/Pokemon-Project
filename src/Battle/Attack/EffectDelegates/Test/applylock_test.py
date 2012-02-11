import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildAttackAction

from Battle.Actions.battle_action import BattleAction
from Battle.Attack.EffectDelegates.applylock_delegate import ApplyLockDelegate

class affectPkmn(unittest.TestCase):
    """ Test cases of affectPkmn """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.target = BuildPokemonBattleWrapper()
        self.turns = 3
        self.delegate = ApplyLockDelegate(self.turns, 0)
        
    def noAction(self):
        """ Test that the Effect fails if the Target has no last Action """
        self.target.lastAction = None
        self.target.actionLock = None
        
        messages = self.delegate.affectPkmn(self.target)
        assert len(messages) == 1, "Should receive one message"
        assert messages[0] == "But it failed", "Should be that the attack failed"
        
    def attackActionApplied(self):
        """ Test that the Action Lock is applied if the Last Action is an Attack Action """
        self.target.lastAction = BuildAttackAction()
        self.target.actionLock = None
        
        messages = self.delegate.affectPkmn(self.target)
        actionLock = self.target.actionLock
        
        assert messages == [], "Should not receive any messages"
        assert actionLock != None, "Should have an action lock"
        assert actionLock.parent == self.target, "Parent should be attached to the target"
        assert actionLock.action == self.target.lastAction, "Action should be the target's last action"
        assert actionLock.turnsToGo == self.turns, "Turns should be the delegates's turns"
        
    def otherActionApplied(self):
        """ Test that the Action Lock is not applied if it is not an Attack Action """
        self.target.lastAction = BattleAction
        self.target.actionLock = None
        
        messages = self.delegate.affectPkmn(self.target)
        actionLock = self.target.actionLock
        
        assert len(messages) == 1, "Should receive one message"
        assert messages[0] == "But it failed", "Should be that the attack failed"
        assert actionLock == None, "Should have an action lock"
        

# Collect all test cases in this class
testcasesAffectPkmn = ["noAction", "attackActionApplied", "otherActionApplied"]
suiteAffectPkmn = unittest.TestSuite(map(affectPkmn, testcasesAffectPkmn))

##########################################################

# Collect all test cases in this file
suites = [suiteAffectPkmn]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()