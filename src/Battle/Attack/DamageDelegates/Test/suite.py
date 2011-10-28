import unittest
import damage_test
import effectiveness_test
import scale_test

suites = [damage_test.suite, effectiveness_test.suite, scale_test.suite]
suite = unittest.TestSuite(suites)