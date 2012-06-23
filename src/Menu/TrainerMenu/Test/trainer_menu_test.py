import unittest
from Test.test_helper import *

from Menu.TrainerMenu.trainer_menu import TrainerMenu

class init(unittest.TestCase):
    """ Test cases of init """
    
    def  setUp(self):
        """ Build the *** for the test """
        
    def trainerEntry(self):
        """ Test that playbale trainer is received """
        menu = TrainerMenu()
        assert menu.entries[0].trainer.title == "Pkmn Trainer", "Didn't get correct title"
        assert menu.entries[0].trainer.name == "Chris", "Didn't get correct name"
        

# Collect all test cases in this class
testcasesInit = ["trainerEntry"]
suiteInit = unittest.TestSuite(map(init, testcasesInit))

##########################################################

# Collect all test cases in this file
suites = [suiteInit]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()