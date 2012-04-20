import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildAttack

from Battle.Attack.EffectDelegates.crash_delegate  import CrashDelegate
from Battle.Status.faint import Faint

class effectOnMiss(unittest.TestCase):
    """ Test cases of effectOnMiss """
    
    def  setUp(self):
        """ Build the Pkmn and Delegate for the test """
        self.pkmn = BuildPokemonBattleWrapper()
        self.attack = BuildAttack()
        
        self.damage, messages = self.attack.damageDelegate.damage(self.pkmn, self.pkmn)
        
        self.ratio = 2
        self.delegate = CrashDelegate(self.attack, self.ratio)
        
    def recoil(self):
        """ Test that recoil damage is done """
        self.pkmn.setCurrHP(self.damage*2)
        self.delegate.effectOnMiss(self.pkmn, self.pkmn)
        
        damageDone = self.damage*2 - self.pkmn.getCurrHP()
        damage = self.damage/self.ratio
        assert damageDone == damage or damageDone == 2*damage, "Should do damage over ratio as damage"
        
    def message(self):
        """ Test that the message returned is correct """
        self.pkmn.setCurrHP(self.damage)
        self.delegate.damage = self.damage
        messages = self.delegate.effectOnMiss(self.pkmn, self.pkmn)

        message = CrashDelegate.message % self.pkmn.getHeader()
        assert len(messages) == 1, "Should get one message"
        assert messages[0] == message, "Message should be Pkmn's header and the Delegate's message"
        
    def faints(self):
        """ Test that the message is correct when the Pkmn faints """
        self.pkmn.setCurrHP(1)
        self.delegate.damage = self.damage
        messages = self.delegate.effectOnMiss(self.pkmn, self.pkmn)

        faintMessage = self.pkmn.getHeader() + Faint.start
        assert len(messages) == 2, "Should get 2 messages"
        assert messages[1] == faintMessage, "Message should be that the Pkmn Fainted"

# Collect all test cases in this class
testcasesEffectOnMiss = ["recoil", "message", "faints"]
suiteEffectOnMiss = unittest.TestSuite(map(effectOnMiss, testcasesEffectOnMiss))

##########################################################

# Collect all test cases in this file
suites = [suiteEffectOnMiss]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()