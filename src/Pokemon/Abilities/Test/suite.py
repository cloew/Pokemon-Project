import unittest

import ability_test
import statmodonstatus_test

suites = [ability_test.suite, statmodonstatus_test.suite]
suite = unittest.TestSuite(suites)