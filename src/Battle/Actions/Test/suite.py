import unittest

from Battle.Actions.Test.action_lock_test import suite as action_lock_suite
from Battle.Actions.Test.battle_action_test import suite as battle_action_suite
from Battle.Actions.Test.attack_action_test import suite as attack_action_suite
from Battle.Actions.Test.switch_action_test import suite as switch_action_suite


suites = [action_lock_suite,
          battle_action_suite, 
          attack_action_suite,
          switch_action_suite]
suite = unittest.TestSuite(suites)