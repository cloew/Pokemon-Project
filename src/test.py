import unittest
import Pokemon.Test.suite
import Pokemon.Abilities.Test.suite
import Trainer.Test.suite
import Battle.Test.suite
import Battle.Actions.Test.suite
import Battle.Attack.Test.suite
import Battle.Attack.DamageDelegates.Test.suite
import Battle.Attack.EffectDelegates.Test.suite
import Battle.Attack.HitDelegates.Test.suite
import Battle.SecondaryEffects.Test.suite
import Battle.Status.Test.suite

# Collect all the test suites
suites = [Pokemon.Test.suite.suite, Pokemon.Abilities.Test.suite.suite,
              Trainer.Test.suite.suite,
              Battle.Test.suite.suite, Battle.Actions.Test.suite.suite,
              Battle.Attack.Test.suite.suite,
              Battle.Attack.DamageDelegates.Test.suite.suite,
              Battle.Attack.EffectDelegates.Test.suite.suite,
              Battle.Attack.HitDelegates.Test.suite.suite,
              Battle.SecondaryEffects.Test.suite.suite,
              Battle.Status.Test.suite.suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
