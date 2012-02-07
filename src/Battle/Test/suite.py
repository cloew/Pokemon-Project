import unittest

import battleside_test
import pkmn_battle_wrapper_test

suites = [battleside_test.suite, pkmn_battle_wrapper_test.suite]
suite = unittest.TestSuite(suites)