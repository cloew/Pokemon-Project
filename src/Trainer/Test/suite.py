import unittest
import trainer_test
import computer_trainer_test
import human_trainer_test
import trainer_factory_test

suites = [trainer_test.suite, computer_trainer_test.suite, human_trainer_test.suite, trainer_factory_test.suite]
suite = unittest.TestSuite(suites)