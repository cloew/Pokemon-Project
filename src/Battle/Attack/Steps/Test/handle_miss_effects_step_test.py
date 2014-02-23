from Battle.Attack.attack import Attack
from Battle.Attack.Steps.handle_miss_effects_step import HandleMissEffectsStep

from Test.test_helper import BuildPokemonBattleWrapper

import unittest

class perform(unittest.TestCase):
    """ Test cases of perform """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.effects = [self, self]
        self.attack.effectDelegates = self.effects
        
        self.step = HandleMissEffectsStep(self.attack)
        
        self.calledApplyEffect = 0
        self.messages = ["My Test Message"]
        
    def applyOnMissFlag(self):
        """ Test that when an effect has the applyOnMiss Flag the effect is used """
        self.applyOnMiss = True
        messages = self.step.perform(None, None, None)
        
        numberOfEffects = len(self.effects)
        self.assertEquals(numberOfEffects, self.calledApplyEffect, "Should have called apply effect for each effect")
        self.assertEquals(self.messages*numberOfEffects, messages, "Should receive the messages from each effect")
        
    def effectOnMissFunction(self):
        """ Test that when an effect has the efffectOnMiss Flag the effect is used """
        self.effectOnMiss = self.applyEffect
        messages = self.step.perform(None, None, None)
        
        numberOfEffects = len(self.effects)
        self.assertEquals(numberOfEffects, self.calledApplyEffect, "Should have called apply effect for each effect")
        self.assertEquals(self.messages*numberOfEffects, messages, "Should receive the messages from each effect")
        
    def otherwise(self):
        """ Test that when an effect has neither Flag nothing happens """
        messages = self.step.perform(None, None, None)
        
        self.assertEquals(0, self.calledApplyEffect, "Should not have called apply effect")
        self.assertEquals([], messages, "Should receive no messages when the effects are prevented")
        
    def applyEffect(self, user, target, environment):
        self.calledApplyEffect += 1
        return self.messages

# Collect all test cases in this class
testcasesPerform = ["applyOnMissFlag", "effectOnMissFunction", "otherwise"]
suitePerform = unittest.TestSuite(map(perform, testcasesPerform))

##########################################################

# Collect all test cases in this file
suites = [suitePerform]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)