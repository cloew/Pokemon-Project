import unittest

import menu_test
import text_menu_entry_test

# from Menu.ActionMenu.Test.suite import suite as action_menu_suite

suites = [menu_test.suite,
          text_menu_entry_test.suite] # ,
          # action_menu_suite]
suite = unittest.TestSuite(suites)