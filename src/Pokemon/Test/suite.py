import unittest
import pokemon_test
import pokemon_battledelegate_test
suites = [pokemon_test.suite, pokemon_battledelegate_test.suite]
suite = unittest.TestSuite(suites)