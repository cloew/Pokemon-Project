import unittest

import menu_test

from Menu.ActionMenu.Test.suite import suite as action_menu_suite

suites = [menu_test.suite,
              action_menu_suite]
suite = unittest.TestSuite(suites)