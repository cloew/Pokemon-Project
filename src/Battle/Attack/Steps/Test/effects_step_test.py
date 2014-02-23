from Battle.Attack.attack import Attack
from Battle.Attack.Steps.effects_step import EffectsStep

from Test.test_helper import BuildPokemonBattleWrapper

import unittest

class perform(unittest.TestCase):
    """ Test cases of perform """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.effects = [self, self]
        self.attack.effectDelegates = self.effects
        
        self.step = EffectsStep(self.attack)
        self.step.preventEffects = self.preventEffects
        
        self.shouldPreventEffects = False
        self.calledApplyEffect = 0
        self.messages = ["My Test Message"]
        
    def effectsPrevented(self):
        """ Test that when effects are prevented everything is handled properly """
        self.shouldPreventEffects = True
        
        messages = self.step.perform(None, None, None)
        
        self.assertEquals(0, self.calledApplyEffect, "Should not have called apply effect")
        self.assertEquals([], messages, "Should receive no messages when the effects are prevented")
        
    def effectsAllowed(self):
        """ Test that when effects are prevented everything is handled properly """
        self.shouldPreventEffects = False
        
        messages = self.step.perform(None, None, None)
        
        numberOfEffects = len(self.effects)
        self.assertEquals(numberOfEffects, self.calledApplyEffect, "Should have called apply effect for each effect")
        self.assertEquals(self.messages*numberOfEffects, messages, "Should receive the messages from each effect")
        
    def preventEffects(self, user, target):
        return self.shouldPreventEffects
        
    def tryToApplyEffect(self, user, target, environment):
        self.calledApplyEffect += 1
        return self.messages

# Collect all test cases in this class
testcasesPerform = ["effectsPrevented", "effectsAllowed"]
suitePerform = unittest.TestSuite(map(perform, testcasesPerform))

##########################################################

class preventEffects(unittest.TestCase):
    """ Test cases of preventEffects """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.attack.damageDelegate = self
        self.step = EffectsStep(self.attack)
        
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
    def userPrevents(self):
        """ Test that when the user prevents effects, the effects can be prevented """
        self.setAbilityCanUseEffectsMethod(self.user, self.cantUseEffects)
        self.setAbilityCanUseEffectsMethod(self.target, self.canUseEffects)
        
        effectsPrevented = self.step.preventEffects(self.user, self.target)
        self.assertTrue(effectsPrevented, "Effects should be prevented")
        
    def targetPrevents(self):
        """ Test that when the target prevents effects, the effects can be prevented """
        self.setAbilityCanUseEffectsMethod(self.user, self.canUseEffects)
        self.setAbilityCanUseEffectsMethod(self.target, self.cantUseEffects)
        
        effectsPrevented = self.step.preventEffects(self.user, self.target)
        self.assertTrue(effectsPrevented, "Effects should be prevented")
        
    def doesDamage(self):
        """ Test that when the attack can do damage, the effects can be prevented """
        self.setAbilityCanUseEffectsMethod(self.user, self.cantUseEffects)
        self.setAbilityCanUseEffectsMethod(self.target, self.cantUseEffects)
        
        effectsPrevented = self.step.preventEffects(self.user, self.target)
        self.assertTrue(effectsPrevented, "Effects should be prevented")
        
    def nullDamage(self):
        """ Test that when the attack cannot do damage, the effects are not prevented """
        self.setAbilityCanUseEffectsMethod(self.user, self.cantUseEffects)
        self.setAbilityCanUseEffectsMethod(self.target, self.cantUseEffects)
        self.isNull = True
        
        effectsPrevented = self.step.preventEffects(self.user, self.target)
        self.assertFalse(effectsPrevented, "Effects should not be prevented")
        
    def abilityDoesNotPrevent(self):
        """ Test that when the abilities cause effects, the effects are not prevented """
        self.setAbilityCanUseEffectsMethod(self.user, self.canUseEffects)
        self.setAbilityCanUseEffectsMethod(self.target, self.canUseEffects)
        
        effectsPrevented = self.step.preventEffects(self.user, self.target)
        self.assertFalse(effectsPrevented, "Effects should not be prevented")
        
    def setAbilityCanUseEffectsMethod(self, pkmn, function):
        pkmn.getAbility().canUseEffects = function
        
    def canUseEffects(self):
        return True
        
    def cantUseEffects(self):
        return False

# Collect all test cases in this class
testcasesPreventEffects = ["userPrevents", "targetPrevents", "doesDamage", "nullDamage", "abilityDoesNotPrevent"]
suitePreventEffects = unittest.TestSuite(map(preventEffects, testcasesPreventEffects))

##########################################################

# Collect all test cases in this file
suites = [suitePerform,
          suitePreventEffects]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)