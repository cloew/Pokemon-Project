import unittest
import leech_test
import periodicheal_test
import trap_test

suites = [leech_test.suite, periodicheal_test.suite, trap_test.suite]
suite = unittest.TestSuite(suites)