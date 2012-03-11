import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildActionLock

from Battle.Attack.attackfactory import AttackFactory
from Battle.Attack.preconditions import PreconditionChecker

class checkLock(unittest.TestCase):
    """ Test cases of checkLock """
    
    def  setUp(self):
        """ Build the Pkmn, Lock, and Precondition Checker for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.actionLock = BuildActionLock(user = self.user)
        self.attack = AttackFactory.getAttackAsNew("TACKLE")
        self.preconditionChecker = PreconditionChecker(self.user, self.target, self.attack)
        
    def hasLock(self):
        """ Test that check lock returns correctly when the user has a lock  """
        self.user.actionLock = self.actionLock
        stop, messages = self.preconditionChecker.checkLock()
        
        message = "{0} USED {1}".format(self.user.getHeader(), self.actionLock.action.attack.name)
        
        assert stop, "Should stop if the user has a lock"
        assert len(messages) > 0,  "Should receive the messages for the actual attack"
        assert messages[0] == message, "Should use the actionLock attack"
        
    def usingLock(self):
        """ Test that check lock returns correctly when the user is using its lock attack  """
        self.preconditionChecker.attack = self.actionLock.action.attack
        self.user.actionLock = self.actionLock
        stop, messages = self.preconditionChecker.checkLock()
        
        message = "{0} USED {1}".format(self.user.getHeader(), self.actionLock.action.attack.name)
        
        assert not stop, "Should not stop if the user is using its lock"
        assert messages == [], "Should not receive any messages"
        
    def noLock(self):
        """ Test that check lock returns correctly when the user has no lock """
        self.user.actionLock = None
        stop, messages = self.preconditionChecker.checkLock()
        
        assert not stop, "Should not stop if the user has no lock"
        assert messages == [], "Should not receive any messages"
        

# Collect all test cases in this class
testcasesCheckLock = ["hasLock", "usingLock", "noLock"]
suiteCheckLock = unittest.TestSuite(map(checkLock, testcasesCheckLock))

##########################################################

class checkFlinch(unittest.TestCase):
    """ Test cases of checkFlinch """
    
    def  setUp(self):
        """ Build the Pkmn and Precondition Checker for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        attack = AttackFactory.getAttackAsNew("TACKLE")
        self.preconditionChecker = PreconditionChecker(self.user, self.target, attack)
        
    def flinching(self):
        """ Test that check flinch returns correctly when the user has is flinching """
        self.user.flinching = True
        stop, messages = self.preconditionChecker.checkFlinch()
        
        message = [self.user.getHeader() + " flinched."]
        
        assert stop, "Should stop if the user flinches"
        assert messages == message, "Should have flinching message"
        
    def notFlinching(self):
        """ Test that check flinch returns correctly when the user is not flinching """
        self.user.flinching = False
        stop, messages = self.preconditionChecker.checkLock()
        
        assert not stop, "Should not stop if the user isn't flinching"
        assert messages == [], "Should not receive any messages"
        

# Collect all test cases in this class
testcasesCheckFlinch = ["flinching", "notFlinching"]
suiteCheckFlinch = unittest.TestSuite(map(checkFlinch, testcasesCheckFlinch))

##########################################################

class checkCharging(unittest.TestCase):
    """ Test cases of checkCharging """
    
    def  setUp(self):
        """ Build the Pkmn and Precondition Checker for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.attack = AttackFactory.getAttackAsNew("DIG")
        self.preconditionChecker = PreconditionChecker(self.user, self.target, self.attack)
        
        attack2 = AttackFactory.getAttackAsNew("TACKLE")
        self.preconditionChecker2 = PreconditionChecker(self.user, self.target, attack2)
        
    def charging(self):
        """ Test that check charging returns correctly when the user is charging  """
        stop, messages = self.preconditionChecker.checkCharging()
        
        message = [self.user.getHeader() + self.attack.effectDelegates[0].message]
        
        assert stop, "Should stop if the user is charging"
        assert messages == message, "Should have charging message"
        
    def notCharging(self):
        """ Test that check charging returns correctly when the user is not charging """
        stop, messages = self.preconditionChecker2.checkCharging()
        
        assert not stop, "Should not stop if the user isn't charging"
        assert messages == [], "Should not receive any messages"
        

# Collect all test cases in this class
testcasesCheckCharging = ["charging", "notCharging"]
suiteCheckCharging = unittest.TestSuite(map(checkCharging, testcasesCheckCharging))

##########################################################

class checkEncore(unittest.TestCase):
    """ Test cases of checkEncore """
    
    def  setUp(self):
        """ Build the Pkmn and Precondition Checker for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.attack = AttackFactory.getAttackAsNew("DIG")
        self.preconditionChecker = PreconditionChecker(self.user, self.target, self.attack)
        
        attack2 = AttackFactory.getAttackAsNew("TACKLE")
        self.preconditionChecker2 = PreconditionChecker(self.user, self.target, attack2)
        
    def encore(self):
        """ Test that check encore returns correctly when the user has an encore  """
        encoreCount = 1
        self.user.encore = encoreCount
        stop, messages = self.preconditionChecker.checkEncore()
        
        message = [self.user.getHeader() + self.attack.effectDelegates[0].message]
        
        assert self.user.encore == encoreCount-1, "Encore should be decremented" 
        assert not stop, "Should never stop if have an encore"
        assert messages == [], "Should not receive any messages"
        
    def noEncore(self):
        """ Test that check encore returns correctly when the user has no encore """
        encoreCount = 0
        self.user.encore = encoreCount
        stop, messages = self.preconditionChecker2.checkEncore()
        
        assert self.user.encore == encoreCount, "Encore should not decrement when there is no encore"
        assert not stop, "Should never stop if have an encore"
        assert messages == [], "Should not receive any messages"
        

# Collect all test cases in this class
testcasesCheckEncore = ["encore", "noEncore"]
suiteCheckEncore = unittest.TestSuite(map(checkEncore, testcasesCheckEncore))

##########################################################

# Collect all test cases in this file
suites = [suiteCheckLock, suiteCheckFlinch, suiteCheckCharging, suiteCheckEncore]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()