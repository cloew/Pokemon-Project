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
        self.action1 = BuildBattleAction(priority = 1)
        self.action2 = BuildBattleAction(priority = 0)
        
    def less(self):
        """ Test that lower priorities return correctly """
        cmp = self.action2.comparePriority(self.action1)
        assert cmp == -1, "Should return -1 when the priority is less"
        
    def more(self):
        """ Test that higher priorities return correctly """
        cmp = self.action1.comparePriority(self.action2)
        assert cmp == 1, "Should return 1 when the priority is more"

# Collect all test cases in this class
testcasesComparePrioirty = ["less", "more"]
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
        
        self.action1 = BuildBattleAction(user = pkmn1)
        self.action2 = BuildBattleAction(user = pkmn2)
        
    def less(self):
        """ Test that lower priorities return correctly """
        cmp = self.action2.compareSpeed(self.action1)
        assert cmp == -1, "Should return -1 when the speed is less"
        
    def more(self):
        """ Test that higher priorities return correctly """
        cmp = self.action1.compareSpeed(self.action2)
        assert cmp == 1, "Should return 1 when the speed is more"

# Collect all test cases in this class
testcasesCompareSpeed = ["less", "more"]
suiteCompareSpeed = unittest.TestSuite(map(compareSpeed, testcasesCompareSpeed))

##########################################################

# Collect all test cases in this file
suites = [suite__cmp__, suiteComparePrioirty, suiteCompareSpeed]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()