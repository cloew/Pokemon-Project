import unittest

import action_lock_test
import attack_action_test


suites = [action_lock_test.suite, attack_action_test.suite]
suite = unittest.TestSuite(suites)