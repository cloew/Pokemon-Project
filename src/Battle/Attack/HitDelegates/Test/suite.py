import unittest
import alwayshit_test
import hit_test
import piercedodge_test
import statushit_test

suites = [alwayshit_test.suite, hit_test.suite, piercedodge_test.suite, statushit_test.suite]
suite = unittest.TestSuite(suites)