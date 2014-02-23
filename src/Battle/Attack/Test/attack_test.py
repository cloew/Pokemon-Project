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
        
    def failPreconditions(self, preconditionChecker, messages):
        self.calledPreconditions = True
        messages.append(self.preconditionMessage)
        return True
        
    def passPreconditions(self, preconditionChecker, messages):
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

class doAttackLoop(unittest.TestCase):
    """ Test cases of doAttackLoop """
    
    def  setUp(self):
        """ Build the Attack for the test """
        self.attack = Attack()
        self.damageMessages = ["My Damage Messages"]
        self.effectMessages = ["My Effect Messages"]
        self.contactMessages = ["My Contact Messages"]
        
        self.calledDoDamage = False
        self.calledDoEffects = False
        self.calledOnContact = False
        
    def makesContact(self):
        """ Test that failing hit prevents the attack loop from being done """
        self.attack.makes_contact = True
        self.attack.doDamage = self.doDamage
        self.attack.doEffects = self.doEffects
        
        self.attack.doAttackLoop(None, self, None)
        
        self.assertTrue(self.calledDoDamage, "Should have called doDamage")
        self.assertTrue(self.calledDoEffects, "Should have called doEffects")
        self.assertTrue(self.calledOnContact, "Should have called onContact")
        
    def noContact(self):
        """ Test that passing hit allows the attack loop to be done """
        self.attack.makes_contact = False
        self.attack.doDamage = self.doDamage
        self.attack.doEffects = self.doEffects
        
        self.attack.doAttackLoop(None, self, None)
        
        self.assertTrue(self.calledDoDamage, "Should have called doDamage")
        self.assertTrue(self.calledDoEffects, "Should have called doEffects")
        self.assertFalse(self.calledOnContact, "Should not have called onContact")
    
    def messagesReturned_NoContact(self):
        """ Test that messages when no contact is made are returned """
        self.attack.makes_contact = False
        self.attack.doDamage = self.doDamage
        self.attack.doEffects = self.doEffects
        
        messages = self.attack.doAttackLoop(None, self, None)
        
        expectedMessages = self.damageMessages + self.effectMessages
        
        for expectedMessage in expectedMessages:
            i = expectedMessages.index(expectedMessage)
            message = messages[i]
            self.assertEquals(expectedMessage, message, "Should have returned each message in the proper order")
        self.assertEquals(len(expectedMessages), len(messages), "Should only have returned the Damage and Effect Messages")
    
    def messagesReturned_OnContact(self):
        """ Test that messages when contact is made are returned """
        self.attack.makes_contact = True
        self.attack.doDamage = self.doDamage
        self.attack.doEffects = self.doEffects
        
        messages = self.attack.doAttackLoop(None, self, None)

        expectedMessages = self.damageMessages + self.effectMessages + self.contactMessages
        
        for expectedMessage in expectedMessages:
            i = expectedMessages.index(expectedMessage)
            message = messages[i]
            self.assertEquals(expectedMessage, message, "Should have returned each message in the proper order")
        self.assertEquals(len(expectedMessages), len(messages), "Should only have returned the Damage, Effect and Contact Messages")
        
    def doDamage(self, user, target, environment):
        self.calledDoDamage = True
        return self.damageMessages
        
    def doEffects(self, user, target, environment):
        self.calledDoEffects = True
        return self.effectMessages
        
    def getAbility(self):
        return self
        
    def onContact(self, target, user):
        self.calledOnContact = True
        return self.contactMessages

# Collect all test cases in this class
testcasesDoAttackLoop = ["makesContact", "makesContact", "messagesReturned_NoContact", "messagesReturned_OnContact"]
suiteDoAttackLoop = unittest.TestSuite(map(doAttackLoop, testcasesDoAttackLoop))

##########################################################

class checkPreconditions(unittest.TestCase):
    """ Test cases of checkPreconditions """
    
    def  setUp(self):
        """ Build the Attack for the test """
        self.attack = Attack()
        self.messages = ["My Test Messages"]
        
        self.calledCheckPreConditions = False
        
    def preconditionsPassthrough(self):
        """ Test that preconditions stop value is returned """
        for stopCondition in [True, False]:
            self.failPreconditions = stopCondition
            stop = self.attack.checkPreconditions(self, [])
        
            self.assertEquals(self.failPreconditions, stop, "Should have returned the failPreconditions parameter")
            self.assertTrue(self.calledCheckPreConditions, "Should have called checkPrecondtitions")
    
    def messagesReturned(self):
        """ Test that messages when no contact is made are returned """
        self.failPreconditions = False
        messages = []
        
        self.attack.checkPreconditions(self, messages)
        
        for expectedMessage in self.messages:
            i = self.messages.index(expectedMessage)
            message = messages[i]
            self.assertEquals(expectedMessage, message, "Should have returned each message in the proper order")
        self.assertEquals(len(self.messages), len(messages), "Should only have returned the Precondtition Messages")
        
    def checkPreConditions(self):
        self.calledCheckPreConditions = True
        return self.failPreconditions, self.messages

# Collect all test cases in this class
testcasesCheckPreconditions = ["preconditionsPassthrough", "messagesReturned"]
suiteCheckPreconditions = unittest.TestSuite(map(checkPreconditions, testcasesCheckPreconditions))

##########################################################

# Collect all test cases in this file
suites = [suiteUse, suiteDoAttack, suiteDoAttackLoop, suiteCheckPreconditions]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)