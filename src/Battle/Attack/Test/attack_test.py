from Battle.Attack.attack import Attack
from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate
from Battle.Attack.DamageDelegates.null_damage_delegate import NullDamageDelegate

import unittest

class MockStep:
    def __init__(self, messages):
        self.messages = messages
        self.performed = False
        
    def perform(self, user, target, environment):
        self.performed = True
        return self.messages

class use(unittest.TestCase):
    """ Test cases of use """
    
    def  setUp(self):
        """ Build the Attack for the test """
        self.attack = Attack()
        self.messages = ["My Test Messages"]
        
        self.attack.preconditionsStep = MockStep(self.messages)
        self.attack.hitStep = MockStep(self.messages)
        self.attack.damageStep = MockStep(self.messages)
        self.attack.effectsStep = MockStep(self.messages)
        self.attack.handleContactStep = MockStep(self.messages)
        self.attack.handleMissEffectsStep = MockStep(self.messages)
        
    def preconditions_Failing(self):
        """ Test that failing precodnitions prevents the attack from being done """
        self.attack.preconditionsStep.passed = False
        
        self.attack.use(None, None, None)
        
        self.assertTrue(self.attack.preconditionsStep.performed, "Should have performed the Precondition Step")
        self.assertFalse(self.attack.hitStep.performed, "Should not have performed the Hit Step")
        self.assertFalse(self.attack.damageStep.performed, "Should not have performed the Damage Step")
        self.assertFalse(self.attack.effectsStep.performed, "Should not have performed the Effects Step")
        self.assertFalse(self.attack.handleContactStep.performed, "Should not have performed the Handle Contact Step")
        self.assertFalse(self.attack.handleMissEffectsStep.performed, "Should not have performed the Hanlde Miss Effects Step")
        
    def hit_Succeeded(self):
        """ Test that passing precodnitions allows the attack to be used """
        self.attack.preconditionsStep.passed = True
        self.attack.hitStep.hit = True
        
        self.attack.use(None, None, None)
        
        self.assertTrue(self.attack.preconditionsStep.performed, "Should have performed the Precondition Step")
        self.assertTrue(self.attack.hitStep.performed, "Should not have performed the Hit Step")
        self.assertTrue(self.attack.damageStep.performed, "Should have performed the Damage Step")
        self.assertTrue(self.attack.effectsStep.performed, "Should have performed the Effects Step")
        self.assertTrue(self.attack.handleContactStep.performed, "Should have performed the Handle Contact Step")
        self.assertFalse(self.attack.handleMissEffectsStep.performed, "Should not have performed the Hanlde Miss Effects Step")
    
    def hit_Missed(self):
        """ Test that messages from the attack are returned """
        self.attack.preconditionsStep.passed = True
        self.attack.hitStep.hit = False
        
        self.attack.use(None, None, None)
        
        self.assertTrue(self.attack.preconditionsStep.performed, "Should have performed the Precondition Step")
        self.assertTrue(self.attack.hitStep.performed, "Should have performed the Hit Step")
        self.assertFalse(self.attack.damageStep.performed, "Should not have performed the Damage Step")
        self.assertFalse(self.attack.effectsStep.performed, "Should not have performed the Effects Step")
        self.assertFalse(self.attack.handleContactStep.performed, "Should not have performed the Handle Contact Step")
        self.assertTrue(self.attack.handleMissEffectsStep.performed, "Should have performed the Hanlde Miss Effects Step")

# Collect all test cases in this class
testcasesUse = ["preconditions_Failing", "hit_Succeeded", "hit_Missed"]
suiteUse = unittest.TestSuite(map(use, testcasesUse))

##########################################################

class isStatus(unittest.TestCase):
    """ Test cases of isStatus """
    
    def  setUp(self):
        """ Build the Attack and Damage Delegate for the test """
        self.attack = Attack()
        self.nullDamageDelegate = NullDamageDelegate()
        self.normalDamageDelegate = DamageDelegate(None, None, None)
        
    def hasNullDamageDelegate(self):
        """ Test that when the damage delegate is the null damage delegate the attack is a status attack """
        self.attack.damageDelegate = self.nullDamageDelegate
        
        isStausAttack = self.attack.isStatus()
        self.assertTrue(isStausAttack, "The Attack should be a status attack")
        
    def hasNormalDamageDelegate(self):
        """ Test that when the damage delegate is normal the attack is not a status attack """
        self.attack.damageDelegate = self.normalDamageDelegate
        
        isStausAttack = self.attack.isStatus()
        self.assertFalse(isStausAttack, "The Attack should not be a status attack")

# Collect all test cases in this class
testcasesIsStatus = ["hasNullDamageDelegate", "hasNormalDamageDelegate"]
suiteIsStatus = unittest.TestSuite(map(isStatus, testcasesIsStatus))

##########################################################

# Collect all test cases in this file
suites = [suiteUse,
          suiteIsStatus]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)