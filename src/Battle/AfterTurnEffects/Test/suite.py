import unittest
import periodicheal_test
import trap_test

suites = [periodicheal_test.suite, trap_test.suite]
suite = unittest.TestSuite(suites)