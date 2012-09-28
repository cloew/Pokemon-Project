import unittest
from Test.test_helper import *

from Menu.ActionMenu.action_menu import ActionMenu

class menuMovement(unittest.TestCase):
    """ Test cases of menuMovement """
    
    def  setUp(self):
        """ Build the Action Menu for the test """
        self.menu = ActionMenu()
        
    def up(self):
        """ Test that up works properly """
        assert self.menu.entries[0].selected, "Should start on first entry"
        self.menu.up()
        assert not self.menu.entries[0].selected, "Should unselect first entry"
        assert self.menu.entries[2].selected, "Should move to third entry"
        self.menu.up()
        assert self.menu.entries[0].selected, "Should move to first entry"
        assert not self.menu.entries[2].selected, "Should unselect third entry"
        
    def down(self):
        """ Test that down works properly """
        assert self.menu.entries[0].selected, "Should start on first entry"
        self.menu.down()
        assert not self.menu.entries[0].selected, "Should unselect first entry"
        assert self.menu.entries[2].selected, "Should move to third entry"
        self.menu.down()
        assert self.menu.entries[0].selected, "Should move to first entry"
        assert not self.menu.entries[2].selected, "Should unselect third entry"
        
    def left(self):
        """ Test that left works properly """
        assert self.menu.entries[0].selected, "Should start on first entry"
        self.menu.left()
        assert not self.menu.entries[0].selected, "Should unselect first entry"
        assert self.menu.entries[1].selected, "Should move to second entry"
        self.menu.left()
        assert self.menu.entries[0].selected, "Should move to first entry"
        assert not self.menu.entries[1].selected, "Should unselect second entry"
        
    def right(self):
        """ Test that right works properly """
        assert self.menu.entries[0].selected, "Should start on first entry"
        self.menu.right()
        assert not self.menu.entries[0].selected, "Should unselect first entry"
        assert self.menu.entries[1].selected, "Should move to second entry"
        self.menu.right()
        assert self.menu.entries[0].selected, "Should move to first entry"
        assert not self.menu.entries[1].selected, "Should unselect second entry"

# Collect all test cases in this class
testcasesMenuMovement = ["up", "down", "left", "right"]
suiteMenuMovement = unittest.TestSuite(map(menuMovement, testcasesMenuMovement))

##########################################################

# Collect all test cases in this file
suites = [suiteMenuMovement]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()