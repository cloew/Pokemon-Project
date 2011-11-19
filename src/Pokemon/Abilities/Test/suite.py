import unittest

import ability_test
import booststab_test
import cantlowerstat_test
import nocrit_test
import sniper_test
import statmodonstatus_test

suites = [ability_test.suite, booststab_test.suite,
              cantlowerstat_test.suite,
              nocrit_test.suite, sniper_test.suite,
              statmodonstatus_test.suite]
              
suite = unittest.TestSuite(suites)