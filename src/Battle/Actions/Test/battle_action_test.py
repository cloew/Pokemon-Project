import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildBattleAction

class __cmp__(unittest.TestCase):
    """ Test cases of __cmp__ """
    
    def  setUp(self):
        """ Build the Action for the test """
        self.action1 = BuildBattleAction(priority = 1)
        self.action2 = BuildBattleAction(priority = 0)
        
    def notImplemented(self):
        """ Test that it returns NotImplemented """
        cmp = self.action1.__cmp__(1)
        assert cmp is NotImplemented, "Should be NotImplemented"
        
    def sortList(self):
        """ Test that it sorts a list properly """
        actions =  [self.action1, self.action2]
        actions.sort()
        assert actions[0] is self.action2, "Should put low priority action to the front"
        assert actions[1] is self.action1, "Should put high priority action to the back"

# Collect all test cases in this class
testcases__cmp__ = ["notImplemented", "sortList"]
suite__cmp__ = unittest.TestSuite(map(__cmp__, testcases__cmp__))

##########################################################

class comparePrioirty(unittest.TestCase):
    """ Test cases of comparePrioirty """
    
    def  setUp(self):
        """ Build the Action for the test """
        self.highPriorityAction = BuildBattleAction(priority = 1)
        self.lowPriorityAction = BuildBattleAction(priority = 0)
        self.lowPriorityAction.compareSpeed = self.compareSpeed
        
        self.calledCompareSpeed = False
        
    def less(self):
        """ Test that lower priorities return correctly """
        cmp = self.lowPriorityAction.comparePriority(self.highPriorityAction)
        assert cmp == -1, "Should return -1 when the priority is less"
        
    def more(self):
        """ Test that higher priorities return correctly """
        cmp = self.highPriorityAction.comparePriority(self.lowPriorityAction)
        assert cmp == 1, "Should return 1 when the priority is more"
        
    def tie(self):
        """ Test that lower priorities return correctly """
        cmp = self.lowPriorityAction.comparePriority(self.lowPriorityAction)
        assert self.calledCompareSpeed, "Should have compared based on speed"
        
    def compareSpeed(self, other):
        self.calledCompareSpeed = True

# Collect all test cases in this class
testcasesComparePrioirty = ["less", "more", "tie"]
suiteComparePrioirty = unittest.TestSuite(map(comparePrioirty, testcasesComparePrioirty))

##########################################################

class compareSpeed(unittest.TestCase):
    """ Test cases of compareSpeed """
    
    def  setUp(self):
        """ Build the Action for the test """
        pkmn1 = BuildPokemonBattleWrapper()
        pkmn2 = BuildPokemonBattleWrapper()
        
        pkmn1.setStat("SPD", 30)
        pkmn2.setStat("SPD", 20)
        
        self.fastAction = BuildBattleAction(user = pkmn1)
        self.slowAction = BuildBattleAction(user = pkmn2)
        
        self.usedRandRange = False
        
    def less(self):
        """ Test that lower priorities return correctly """
        cmp = self.slowAction.compareSpeed(self.fastAction)
        assert cmp == -1, "Should return -1 when the speed is less"
        
    def more(self):
        """ Test that higher priorities return correctly """
        cmp = self.fastAction.compareSpeed(self.slowAction)
        assert cmp == 1, "Should return 1 when the speed is more"
        
    def tie(self):
        """ Test that higher priorities return correctly """
        cmp = self.fastAction.compareSpeed(self.fastAction, random=self)
        assert self.usedRandRange, "Should have picked a random action to win"
        assert range(self.bottom, self.top, self.step) == [-1, 1], "Should have tried to pick valid random value"
        
    def randrange(self, bottom, top, step):
        self.bottom = bottom
        self.top = top
        self.step = step
        self.usedRandRange = True

# Collect all test cases in this class
testcasesCompareSpeed = ["less", "more", "tie"]
suiteCompareSpeed = unittest.TestSuite(map(compareSpeed, testcasesCompareSpeed))

##########################################################

# Collect all test cases in this file
suites = [suite__cmp__, suiteComparePrioirty, suiteCompareSpeed]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()