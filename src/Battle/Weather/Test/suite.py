import unittest

import hail_test
import weather_test

suites = [hail_test.suite,
          weather_test.suite]
suite = unittest.TestSuite(suites)