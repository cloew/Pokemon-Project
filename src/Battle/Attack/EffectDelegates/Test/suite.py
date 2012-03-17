import unittest
import applylock_test
import applystatus_test
import chance_test
import charge_test
import confuse_test
import critmod_test
import curestatus_test
import dodge_test
import effect_delegate_test
import encore_test
import flinch_test
import heal_damageratio_test
import heal_hpratio_test
import heal_ratio_test
import leechdelegate_test
import periodichealdelegate_test
import randomstatmod_test
import recoil_test
import reset_statmods_test
import selfdestruct_test
import statmod_test
import swapstatmods_test
import trapdelegate_test

suites = [applylock_test.suite, applystatus_test.suite,
              chance_test.suite, charge_test.suite, 
              confuse_test.suite, critmod_test.suite,
              curestatus_test.suite, dodge_test.suite,
              effect_delegate_test.suite,
              encore_test.suite, flinch_test.suite,
              heal_damageratio_test.suite,
              heal_hpratio_test.suite, heal_ratio_test.suite,
              leechdelegate_test.suite,
              periodichealdelegate_test.suite,
              randomstatmod_test.suite, recoil_test.suite,
              reset_statmods_test.suite, selfdestruct_test.suite,
              statmod_test.suite,
              swapstatmods_test.suite, trapdelegate_test.suite]
suite = unittest.TestSuite(suites)