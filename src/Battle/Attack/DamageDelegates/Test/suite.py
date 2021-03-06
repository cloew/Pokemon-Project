import unittest

import boost_on_status_test
import damage_test
import effectiveness_test
import effect_ondamage_test
import fixed_test
import halfhealth_test
import level_test
import no_faint_test
import null_damage_test
import onehit_test
import piercedodge_2Xtest
import scale_test
import statratio_test
import statratio_fixed_test
import statratio_range_test

suites = [boost_on_status_test.suite, damage_test.suite, effectiveness_test.suite, effect_ondamage_test.suite,
              fixed_test.suite, halfhealth_test.suite, level_test.suite, no_faint_test.suite, null_damage_test.suite,
              onehit_test.suite, piercedodge_2Xtest.suite, scale_test.suite, statratio_test.suite,
              statratio_fixed_test.suite,
              statratio_range_test.suite]
suite = unittest.TestSuite(suites)