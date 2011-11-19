from Pokemon.Abilities.booststab_ability import BoostStabAbility

import unittest

class onStab(unittest.TestCase):
    """ Test that onStab returns the correct mods """
    
    def setUp(self):
        """ Builds the delegate and side for use in the tests """
        self.ability = BoostStabAbility("")
        
    def properReturnValues(self):
        """ Check that onStatMod returns the proper default values """
        mod = self.ability.onStab()
        
        assert mod == BoostStabAbility.stabMod, "Stab Mod should be mod from BoostStabAbility."
        
testcasesOnStab = ["properReturnValues"]
suiteOnStab = unittest.TestSuite(map(onStab, testcasesOnStab))

##########################################################

 
suites = [suiteOnStab]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()