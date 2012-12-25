import unittest

from Trainer.human_trainer import HumanTrainer

class getHeader(unittest.TestCase):
    """ Test cases of getHeader """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = HumanTrainer()
        
    def headerIsHumanHeader(self):
        """ Check that the attack returned by getAction is an attack the Pokemon has """
        assert self.trainer.getHeader() is HumanTrainer.header, "Should be an empty string"

# Collect all test cases in this class
testcasesGetHeader = ["headerIsHumanHeader"]
suiteGetHeader   = unittest.TestSuite(map(getHeader , testcasesGetHeader ))

##########################################################
# Collect all test cases in this file
suites = [suiteGetHeader]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()