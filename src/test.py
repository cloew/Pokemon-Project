import unittest
import Menu.Test.suite
import Menu.TrainerMenu.Test.trainer_menu_test
import Pokemon.Test.suite
import Pokemon.Abilities.Test.suite
import Trainer.Test.suite
import Battle.Test.suite
import Battle.Attack.CritDelegates.Test.suite
import Battle.Attack.DamageDelegates.Test.suite
import Battle.Attack.EffectDelegates.Test.suite
import Battle.Attack.HitDelegates.Test.suite
import Battle.FaintHandlers.Test.suite
import Battle.SecondaryEffects.Test.suite
import Battle.Status.Test.suite

from Screen.Console.window import window

# Collect all the test suites
suites = [Menu.Test.suite.suite,
          Menu.TrainerMenu.Test.trainer_menu_test.suite,
          Pokemon.Test.suite.suite,
          Pokemon.Abilities.Test.suite.suite,
          Trainer.Test.suite.suite,
          Battle.Test.suite.suite,
          Battle.Attack.CritDelegates.Test.suite.suite,
          Battle.Attack.DamageDelegates.Test.suite.suite,
          Battle.Attack.EffectDelegates.Test.suite.suite,
          Battle.Attack.HitDelegates.Test.suite.suite,
          Battle.FaintHandlers.Test.suite.suite,
          Battle.SecondaryEffects.Test.suite.suite,
          Battle.Status.Test.suite.suite]

try:
    alltests = unittest.TestSuite(suites)
finally:
    window.close()

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
