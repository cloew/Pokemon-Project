import unittest
import applylock_test
import applystatus_test
import chance_test
import charge_test
import confuse_test
import curestatus_test
import leechdelegate_test
import periodichealdelegate_test
import randomstatmod_test
import statmod_test
import swapstatmods_test
import trapdelegate_test

suites = [applylock_test.suite, applystatus_test.suite,
              chance_test.suite, charge_test.suite, 
              confuse_test.suite, curestatus_test.suite,
              leechdelegate_test.suite,
              periodichealdelegate_test.suite,
              randomstatmod_test.suite,
              statmod_test.suite,
              swapstatmods_test.suite, trapdelegate_test.suite]
suite = unittest.TestSuite(suites)