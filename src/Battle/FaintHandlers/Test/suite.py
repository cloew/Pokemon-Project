import unittest

import either_faint_test
import faint_handler_test
import target_faint_test
import user_faint_test

suites = [either_faint_test.suite, faint_handler_test.suite,
              target_faint_test.suite, user_faint_test.suite]
suite = unittest.TestSuite(suites)