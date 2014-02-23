import unittest

from Battle.Attack.Test.attack_test import suite as attack_suite
from Battle.Attack.Test.preconditions_test import suite as preconditions_suite

suites = [attack_suite,
          preconditions_suite]
suite = unittest.TestSuite(suites)