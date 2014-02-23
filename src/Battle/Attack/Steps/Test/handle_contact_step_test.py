from Battle.Attack.attack import Attack
from Battle.Attack.Steps.handle_contact_step import HandleContactStep

from Test.test_helper import BuildPokemonBattleWrapper

import unittest

class perform(unittest.TestCase):
    """ Test cases of perform """
    
    def  setUp(self):
        """ Build the Step for the test """
        self.attack = Attack()
        self.step = HandleContactStep(self.attack)
        
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.user.getAbility().onContact = self.onContact
        self.target.getAbility().onContact = self.onContact
        
        self.hitPkmn = None
        self.calledOnContact = 0
        self.messages = ["My Test Message"]
        
    def makesContact(self):
        """ Test that when the attack makes contact the targets contact effect is used """
        self.attack.makes_contact = True
        
        messages = self.step.perform(self.user, self.target, None)
        
        self.assertIs(self.target, self.hitPkmn, "Should have called onContact for the Target Pkmn")
        self.assertEquals(1, self.calledOnContact, "Should have called onContact only once")
        self.assertEquals(self.messages, messages, "Should receive messages from the onContact")
        
    def doesNotMakeContact(self):
        """ Test that when the attack does not make contact nothing happens """
        self.attack.makes_contact = False
        
        messages = self.step.perform(self.user, self.target, None)
        
        self.assertEquals(0, self.calledOnContact, "Should not have called onContact")
        self.assertEquals([], messages, "Should receive no messages")
        
    def onContact(self, pkmnHit, pkmnWhoAttacked):
        self.hitPkmn = pkmnHit
        self.calledOnContact += 1
        return self.messages

# Collect all test cases in this class
testcasesPerform = ["makesContact", "doesNotMakeContact"]
suitePerform = unittest.TestSuite(map(perform, testcasesPerform))

##########################################################

# Collect all test cases in this file
suites = [suitePerform]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)