import unittest
from Test.test_helper import *

from Trainer.trainer_factory import TrainerFactory

class getPlayableTrainers(unittest.TestCase):
    """ Test cases of getPlayableTrainers """
    
    def  setUp(self):
        """ Build the *** for the test """
        
    def receivedPlayableTrainer(self):
        """ Test that the playable trainers are received """
        playableTrainers = TrainerFactory.getPlayableTrainers()
        assert playableTrainers[0].title == "Pkmn Trainer", "Didn't get correct title"
        assert playableTrainers[0].name == "Chris", "Didn't get correct name"

# Collect all test cases in this class
testcasesGetPlayableTrainers = ["receivedPlayableTrainer"]
suiteGetPlayableTrainers = unittest.TestSuite(map(getPlayableTrainers, testcasesGetPlayableTrainers))

##########################################################

# Collect all test cases in this file
suites = [suiteGetPlayableTrainers]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()