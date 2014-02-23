import unittest

import battle_environment_test
import battle_message_test
import battleside_test
import pkmn_battle_wrapper_test

from Battle.Actions.Test.suite import suite as action_suite
from Battle.Weather.Test.suite import suite as weather_suite

suites = [battle_environment_test.suite,
          battle_message_test.suite,
          battleside_test.suite,
          pkmn_battle_wrapper_test.suite,
          action_suite,
          weather_suite]
suite = unittest.TestSuite(suites)