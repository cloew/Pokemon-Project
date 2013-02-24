import unittest

import ability_test
import accmod_test
import booststab_test
import cantlowerstat_test
import confusion_immunity_ability_test
import nocrit_test
import skipturn_test
import sniper_test
import statmodonstatus_test

suites = [ability_test.suite, accmod_test.suite,
              booststab_test.suite,
              cantlowerstat_test.suite,
              confusion_immunity_ability_test.suite,
              nocrit_test.suite, skipturn_test.suite,
              sniper_test.suite,
              statmodonstatus_test.suite]
              
suite = unittest.TestSuite(suites)