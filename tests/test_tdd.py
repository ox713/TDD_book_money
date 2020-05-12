import unittest
import os
import sys
# sys.path.append(os.getcwd())
from TDD import *


class TestTdd(unittest.TestCase):
    def test_mul(self):
        # объект не должен меняться при взаимодействии
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    # использование паттерна объект-значение для тогочтобы 5 д были 5 до
    def test_equality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))

if __name__ == "__main__":
    unittest.main()