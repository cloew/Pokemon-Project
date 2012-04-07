import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.EffectDelegates.multi_turn_delegate import MultiTurnDelegate

class incTurns(unittest.TestCase):
    """ Test cases of incTurns """
    
    def  setUp(self):
        """ Build the Delegate for the test """
        self.turns = 2
        self.delegate = MultiTurnDelegate(self.turns, None)
        
    def inc(self):
        """ Test that the turnOn is incremented """
        self.delegate.turnOn = 0
        self.delegate.incTurns()
        
        assert self.delegate.turnOn == 1, "Turn should be incremented"
        
    def wrapAround(self):
        """ Test that the turnOn wraps around to 0 when it hits the turn count """
        self.delegate.turnOn = self.turns - 1
        self.delegate.incTurns()
        
        assert self.delegate.turnOn == 0, "Turn should wrap around to 0"

# Collect all test cases in this class
testcasesIncTurns = ["inc", "wrapAround"]
suiteIncTurns = unittest.TestSuite(map(incTurns, testcasesIncTurns))

##########################################################

class applyLock(unittest.TestCase):
    """ Test cases of applyLock """
    
    def  setUp(self):
        """ Build the Delegate for the test """
        self.user = BuildPokemonBattleWrapper()
        self.lastAction = 2
        self.user.lastAction = self.lastAction
        
        self.turns = 2
        self.delegate = MultiTurnDelegate(self.turns, None)
        
        self.delegate.applyLock(self.user)
        self.actionLock = self.user.actionLock
        
    def parent(self):
        """ Test that the parent is the effect's user """
        assert self.actionLock.parent == self.user, "Lock's parent should be the using Pkmn"
        
    def action(self):
        """ Test that the action is the user's last action """
        assert self.actionLock.action == self.lastAction, "Lock's action should be the user's last action"
        
    def turnsToGo(self):
        """ Test that the turnsToGo are the effect's turns - 1 """
        assert self.actionLock.turnsToGo == self.turns -1, "Lock's turns to go should be effect's turns -1 since the effect has actually already done one of its chain"

# Collect all test cases in this class
testcasesApplyLock = ["parent", "action", "turnsToGo"]
suiteApplyLock = unittest.TestSuite(map(applyLock, testcasesApplyLock))

##########################################################

# Collect all test cases in this file
suites = [suiteIncTurns, suiteApplyLock]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()