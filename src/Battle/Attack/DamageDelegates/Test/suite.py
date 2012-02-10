import unittest

import damage_test
import effectiveness_test
import effect_ondamage_test
import fixed_test
import halfhealth_test
import level_test
import null_damage_test
import onehit_test
import scale_test
import statratio_test

suites = [damage_test.suite, effectiveness_test.suite, effect_ondamage_test.suite,
              fixed_test.suite, halfhealth_test.suite, level_test.suite, null_damage_test.suite,
              onehit_test.suite, scale_test.suite, statratio_test.suite]
suite = unittest.TestSuite(suites)