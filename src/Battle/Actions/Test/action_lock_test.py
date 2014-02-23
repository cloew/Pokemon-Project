import unittest

from Battle.Actions.action_lock import ActionLock
from Battle.Actions.attack_action import AttackAction
from Battle.Attack.attackfactory import AttackFactory

class useAction(unittest.TestCase):
    """ Tests cases of the useAction function """
    
    def setUp(self):
        """ Build action for the test"""
        attack = AttackFactory.getAttackAsNew("TACKLE")
        self.action = AttackAction(attack, None, None, None)
        self.turns = 2
        self.actionLock = ActionLock(self, self.action, self.turns)
        
    def actionReturned(self):
        """ Checks if useAction returns the proper Action """
        action = self.actionLock.useAction()
        
        assert action is self.action, "Action should be the action the lock was built with"
        
    def turnsDecreased(self):
        """ Checks that the turns counter is decreased """
        action = self.actionLock.useAction()
        
        assert self.actionLock.turnsToGo == self.turns-1, \
            "turnsToGo in the lock should be decresed by 1"
            
    def parentLockRemoved_unfinished(self):
        """ Checks if useAction changes variables appropriately """
        self.actionLock.turnsToGo = 2
        action = self.actionLock.useAction()
        
        assert self.actionLock is not None, "Parent action lock should remain when not finished"
            
    def parentLockRemoved_finished(self):
        """ Checks if useAction changes variables appropriately """
        self.actionLock.turnsToGo = 1
        action = self.actionLock.useAction()
        
        assert self.actionLock is None, "Parent action lock should be removed when finished"
        
# Collect all test cases in this class
testcasesUseAction = ["actionReturned", "turnsDecreased", "parentLockRemoved_unfinished", "parentLockRemoved_finished"]
suiteUseAction = unittest.TestSuite(map(useAction, testcasesUseAction))

##########################################################

class done(unittest.TestCase):
    """ Tests cases of the done function """

    def setUp(self):
        """ Build action for the tests"""
        self.doneLock = ActionLock(None, None, 0)
        self.notDoneLock = ActionLock(None, None, 1)
    
    def isDone(self):
        """ Test that done returns true correctly """
        assert self.doneLock.done(), "Lock with 0 turns should be done"
        
    def notDone(self):
        """ Test that done returns true correctly """
        assert not self.notDoneLock.done(), \
            "Lock with more than 0 turns should not be done"
        
    
# Collect all test cases in this class
testcasesDone = ["isDone", "notDone"]
suiteDone = unittest.TestSuite(map(done, testcasesDone))

##########################################################
# Collect all test cases in this file
suites = [suiteUseAction, suiteDone]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()