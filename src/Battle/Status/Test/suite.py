import unittest
import burn_test
import freeze_test
import paralysis_test
import poison_test
import sleep_test
import status_test
import toxicpoison_test

suites = [burn_test.suite, freeze_test.suite, paralysis_test.suite,
             poison_test.suite, sleep_test.suite, status_test.suite,
             toxicpoison_test.suite]
suite = unittest.TestSuite(suites)