import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate
from Battle.Attack.DamageDelegates.boost_on_status_delegate import BoostDamageOnStatusDelegate

from Battle.Status.status import Status
from Battle.Status.burn import Burn

class coreDamage(unittest.TestCase):
    """ Test that core damage is calculated correctly """ 
    
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        regDelegate = DamageDelegate(None, 50, 1)
        self.core = regDelegate.coreDamage(self.user, self.target)
        
        self.delegate = BoostDamageOnStatusDelegate(None, 50, 1)
        
    def noStatus(self):
        """ Test that damage is core when the target has no status """
        self.target.setStatus(Status())
        damage = self.delegate.coreDamage(self.user, self.target)
        
        assert damage == self.core, "Damage should be the core when target has no status"
        
    def status(self):
        """ Test that damage is double the core when the target has a status """
        self.target.setStatus(Burn())
        damage = self.delegate.coreDamage(self.user, self.target)
        
        assert damage == 2*self.core, "Damage should double when target has a status"

# Collect all test cases in this class      
testcasesCoreDamage = ["noStatus", "status"]
suiteCoreDamage = unittest.TestSuite(map(coreDamage, testcasesCoreDamage))

#########################################################

# Collect all test cases in this file
suites = [suiteCoreDamage]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()