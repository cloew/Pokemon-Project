import unittest

from Battle.Attack.Steps.Test.suite import suite as steps_suite
from Battle.Attack.Test.attack_test import suite as attack_suite
from Battle.Attack.Test.preconditions_test import suite as preconditions_suite

suites = [attack_suite,
          preconditions_suite,
          steps_suite]
suite = unittest.TestSuite(suites)