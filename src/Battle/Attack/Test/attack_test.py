from Battle.Attack.attack import Attack

import unittest

class use(unittest.TestCase):
    """ Test cases of use """
    
    def  setUp(self):
        """ Build the Attack for the test """
        self.attack = Attack()
        self.messages = ["My Test Messages"]
        self.preconditionMessage = "My Precondition Message"
        
        self.calledPreconditions = False
        self.calledDoAttack = False
        
    def preconditions_Failing(self):
        """ Test that failing precodnitions prevents the attack from being done """
        self.attack.checkPreconditions = self.failPreconditions
        self.attack.doAttack = self.doAttack
        
        self.attack.use(None, None, None)
        
        self.assertTrue(self.calledPreconditions, "Should have called checkPreconditions")
        self.assertFalse(self.calledDoAttack, "Should not have called doAttack")
        
    def preconditions_Passing(self):
        """ Test that passing precodnitions allows the attack to be used """
        self.attack.checkPreconditions = self.passPreconditions
        self.attack.doAttack = self.doAttack
        
        self.attack.use(None, None, None)
        
        self.assertTrue(self.calledPreconditions, "Should have called checkPreconditions")
        self.assertTrue(self.calledDoAttack, "Should have called doAttack")
    
    def messagesReturned_Failing(self):
        """ Test that messages from the attack are returned """
        self.attack.checkPreconditions = self.failPreconditions
        self.attack.doAttack = self.doAttack
        
        messages = self.attack.use(None, None, None)
        
        self.assertIn(self.preconditionMessage, messages, "Should have returned the message from the Preconditions check")
        self.assertEquals(1, len(messages), "Should only have returned the Preconditions Messages")
    
    def messagesReturned_Passing(self):
        """ Test that messages from the attack are returned """
        self.attack.checkPreconditions = self.passPreconditions
        self.attack.doAttack = self.doAttack
        
        messages = self.attack.use(None, None, None)

        expectedMessages = self.messages + [self.preconditionMessage]
        
        self.assertIn(self.preconditionMessage, messages, "Should have returned the message from the Preconditions check")
        for message in expectedMessages:
            self.assertIn(message, messages, "Should have returned each message from the Attack")
        self.assertEquals(len(expectedMessages), len(messages), "Should only have returned the Precondition and Attack Messages")
        
    def failPreconditions(self, user, target, environment, messages):
        self.calledPreconditions = True
        messages.append(self.preconditionMessage)
        return True
        
    def passPreconditions(self, user, target, environment, messages):
        self.calledPreconditions = True
        messages.append(self.preconditionMessage)
        return False
        
    def doAttack(self, user, target, environment):
        self.calledDoAttack = True
        return self.messages

# Collect all test cases in this class
testcasesUse = ["preconditions_Failing", "preconditions_Passing", "messagesReturned_Failing", "messagesReturned_Passing"]
suiteUse = unittest.TestSuite(map(use, testcasesUse))

##########################################################

# Collect all test cases in this file
suites = [suiteUse]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)