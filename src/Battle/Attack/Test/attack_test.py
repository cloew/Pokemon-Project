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

class doAttack(unittest.TestCase):
    """ Test cases of doAttack """
    
    def  setUp(self):
        """ Build the Attack for the test """
        self.attack = Attack()
        self.attack.name = "Test Attack"
        self.messages = ["My Test Messages"]
        self.hitMessage = "My Precondition Message"
        self.attackUsedMessage = "%s USED %s" % (self.getHeader(), self.attack.name)
        
        self.calledDoHit = False
        self.calledDoAttackLoop = False
        
    def hit_Failing(self):
        """ Test that failing hit prevents the attack loop from being done """
        self.attack.doHit = self.failHit
        self.attack.doAttackLoop = self.doAttackLoop
        
        self.attack.doAttack(self, None, None)
        
        self.assertTrue(self.calledDoHit, "Should have called doHit")
        self.assertFalse(self.calledDoAttackLoop, "Should not have called doAttackLoop")
        
    def hit_Passing(self):
        """ Test that passing hit allows the attack loop to be done """
        self.attack.doHit = self.passHit
        self.attack.doAttackLoop = self.doAttackLoop
        
        self.attack.doAttack(self, None, None)
        
        self.assertTrue(self.calledDoHit, "Should have called doHit")
        self.assertTrue(self.calledDoAttackLoop, "Should have called doAttackLoop")
    
    def messagesReturned_Failing(self):
        """ Test that messages from the hit attempt are returned """
        self.attack.doHit = self.failHit
        self.attack.doAttackLoop = self.doAttackLoop
        
        messages = self.attack.doAttack(self, None, None)
        
        self.assertEquals(self.attackUsedMessage, messages[0], "Should have returned the attack used message")
        self.assertEquals(self.hitMessage, messages[1], "Should have returned the message from the Hit check")
        self.assertEquals(2, len(messages), "Should only have returned the Attack Used & Hit Messages")
    
    def messagesReturned_Passing(self):
        """ Test that messages from the attack and hit attempt are returned """
        self.attack.doHit = self.passHit
        self.attack.doAttackLoop = self.doAttackLoop
        
        messages = self.attack.doAttack(self, None, None)

        expectedMessages = [self.attackUsedMessage, self.hitMessage] + self.messages
        
        for expectedMessage in expectedMessages:
            i = expectedMessages.index(expectedMessage)
            message = messages[i]
            self.assertEquals(expectedMessage, message, "Should have returned each message in the proper order")
        self.assertEquals(len(expectedMessages), len(messages), "Should only have returned the Attack Used, Hit and Attack Messages")
        
    def failHit(self, user, target, environment, messages):
        self.calledDoHit = True
        messages.append(self.hitMessage)
        return False
        
    def passHit(self, user, target, environment, messages):
        self.calledDoHit = True
        messages.append(self.hitMessage)
        return True
        
    def doAttackLoop(self, user, target, environment):
        self.calledDoAttackLoop = True
        return self.messages
        
    def getHeader(self):
        return "My Header"

# Collect all test cases in this class
testcasesDoAttack = ["hit_Failing", "hit_Passing", "messagesReturned_Failing", "messagesReturned_Passing"]
suiteDoAttack = unittest.TestSuite(map(doAttack, testcasesDoAttack))

##########################################################

# Collect all test cases in this file
suites = [suiteUse, suiteDoAttack]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)