import unittest

from Battle.Attack.Steps.Test.announcement_step_test import suite as announcement_step_suite
from Battle.Attack.Steps.Test.hit_step_test import suite as hit_step_suite
from Battle.Attack.Steps.Test.precondition_step_test import suite as precondition_step_suite

suites = [precondition_step_suite,
          hit_step_suite,
          announcement_step_suite]
suite = unittest.TestSuite(suites)