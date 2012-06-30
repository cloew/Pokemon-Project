import unittest

import battle_message_test
import battleside_test
import pkmn_battle_wrapper_test

suites = [battle_message_test.suite,
             battleside_test.suite,
             pkmn_battle_wrapper_test.suite]
suite = unittest.TestSuite(suites)