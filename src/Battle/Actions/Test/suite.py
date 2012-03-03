import unittest

import action_lock_test
import battle_action_test
import attack_action_test


suites = [action_lock_test.suite, battle_action_test.suite, attack_action_test.suite]
suite = unittest.TestSuite(suites)