import unittest

from Battle.AfterTurnEffect.Test.after_turn_effect_test import suite as after_turn_effect_suite

suites = [after_turn_effect_suite]
suite = unittest.TestSuite(suites)