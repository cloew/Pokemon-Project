import unittest

import affect_user_faint_test
import either_faint_test
import faint_handler_test
import target_faint_test
import user_faint_test

suites = [affect_user_faint_test.suite,
              either_faint_test.suite, 
              faint_handler_test.suite,
              target_faint_test.suite, 
              user_faint_test.suite]
suite = unittest.TestSuite(suites)