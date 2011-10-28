from Battle.Attack.DamageDelegates.effectiveness import Effectiveness

import unittest

class getMod(unittest.TestCase):
    """ Test the getMod function """
    
    def immune(self):
        """ Test that the correct values are returned when the 
        Pokemon is immune to the Attack Type """
        mod = Effectiveness.getMod("GHOST", "NORMAL")
        assert mod is 0, "GHOST on NORMAL should be immune"
        
    def ineffective(self):
        """ Test that the correct values are returned when the 
        Pokemon is resistant to the Attack Type """
        mod = Effectiveness.getMod("FIRE", "FIRE")
        assert mod == .5, "FIRE on FIRE should be ineffective"
        
    def effective(self):
        """ Test that the correct values are returned when the 
        Pokemon is indifferent to the Attack Type """
        mod = Effectiveness.getMod("NORMAL", "NORMAL")
        assert mod is 1, "NORMAL on NORMAL should be effective"
        
    def supereffective(self):
        """ Test that the correct values are returned when the 
        Pokemon is weak to the Attack Type """
        mod = Effectiveness.getMod("FIRE", "ICE")
        assert mod is 2, "FIRE on ICE should be super-effective"
       
# Collect all test cases for this class       
testcasesGetMod = ["immune", "ineffective", "effective", "supereffective"]
suiteGetMod = unittest.TestSuite(map(getMod, testcasesGetMod))

#########################################################

class respond(unittest.TestCase):
    """ Test the respondfunction """
    
    def immune(self):
        """ Test that the correct values are returned when the 
        Pokemon is immune to the Attack Type """
        message = Effectiveness.respond(0)
        assert message == Effectiveness.immuneResponse, \
                "Response should be the immune response"
        
    def ineffective(self):
        """ Test that the correct values are returned when the 
        Pokemon is resistant to the Attack Type """
        message = Effectiveness.respond(.25)
        assert message == Effectiveness.ineffectiveResponse, \
                "Response should be the ineffective response"
        message = Effectiveness.respond(.5)
        assert message == Effectiveness.ineffectiveResponse, \
                "Response should be the ineffective response"
        
    def effective(self):
        """ Test that the correct values are returned when the 
        Pokemon is indifferent to the Attack Type """
        message = Effectiveness.respond(1)
        assert message == Effectiveness.effectiveResponse, \
                "Response should be the effective response"
        
    def supereffective(self):
        """ Test that the correct values are returned when the 
        Pokemon is weak to the Attack Type """
        message = Effectiveness.respond(2)
        assert message == Effectiveness.superEffectiveResponse, \
                "Response should be the super-effective response"
        message = Effectiveness.respond(4)
        assert message == Effectiveness.superEffectiveResponse,  \
                "Response should be the super-effective response"
       
# Collect all test cases in this class      
testcasesRespond = ["immune", "ineffective", "effective", "supereffective"]
suiteRespond = unittest.TestSuite(map(respond, testcasesRespond))

#########################################################

class getEffectiveness(unittest.TestCase):
    """ Test the getMod function """
    def setUp(self):
        self.typeImmune = ["GHOST", "NORMAL"]
        self.typeIneffective = ["FIRE"]
        self.typeIneffective2 = ["FIRE", "ROCK"]
        self.typeEffective = ["NORMAL"]
        self.typeSuperEffective = ["ICE"]
        self.typeSuperEffective2 = ["ICE", "GRASS"]
    
    def immune(self):
        """ Test that the correct values are returned when the 
        Pokemon is immune to the Attack Type """
        mod, message = Effectiveness.getEffectiveness("GHOST", self.typeImmune)
        assert mod is 0, "GHOST on NORMAL should be immune"
        
    def ineffective(self):
        """ Test that the correct values are returned when the 
        Pokemon is resistant to the Attack Type """
        mod, message = Effectiveness.getEffectiveness("FIRE", self.typeIneffective)
        assert mod == .5, "FIRE on FIRE should be ineffective"
        
        mod, message = Effectiveness.getEffectiveness("FIRE", self.typeIneffective2)
        assert mod == .25, "FIRE on FIRE/ROCK should be 2x ineffective"
        
    def effective(self):
        """ Test that the correct values are returned when the 
        Pokemon is indifferent to the Attack Type """
        mod, message = Effectiveness.getEffectiveness("NORMAL", self.typeEffective)
        assert mod is 1, "NORMAL on NORMAL should be effective"
        assert message is None,  \
                "No message should be returned when the attack is unmodified"
        
    def supereffective(self):
        """ Test that the correct values are returned when the 
        Pokemon is weak to the Attack Type """
        mod, message = Effectiveness.getEffectiveness("FIRE", self.typeSuperEffective)
        assert mod is 2, "FIRE on ICE should be super-effective"
        
        mod, message = Effectiveness.getEffectiveness("FIRE", self.typeSuperEffective2)
        assert mod is 4, "FIRE on ICE/GRASS should be 2x super-effective"
        
# Collect all test cases in this class      
testcasesGetEffectiveness = ["immune", "ineffective", "effective", "supereffective"]
suiteGetEffectiveness = unittest.TestSuite(map(getEffectiveness, testcasesGetEffectiveness))

#########################################################

suites = [suiteGetMod, suiteRespond, suiteGetEffectiveness]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()