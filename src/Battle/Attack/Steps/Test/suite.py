import unittest

from Battle.Attack.Steps.Test.precondition_step_test import suite as precondition_step_suite

suites = [precondition_step_suite]
suite = unittest.TestSuite(suites)