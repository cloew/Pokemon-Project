import unittest
import applystatus_test
import charge_test
import leechdelegate_test
import periodichealdelegate_test
import statmod_test
import swapstatmods_test
import trapdelegate_test

suites = [applystatus_test.suite, charge_test.suite, 
              leechdelegate_test.suite,
              periodichealdelegate_test.suite, statmod_test.suite,
              swapstatmods_test.suite, trapdelegate_test.suite]
suite = unittest.TestSuite(suites)