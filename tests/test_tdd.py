import unittest
import os
import sys
# sys.path.append(os.getcwd())
from TDD import *


class TestTdd(unittest.TestCase):
    def test_mul(self):
        five = Dollar(5)
        # повышение понятности тестов, сравниваем доллар с долларом
        # избавились от ненужной переменной product
        self.assertEqual(Dollar(10).amount, five.times(2).amount)
        product = five.times(3)
        self.assertEqual(Dollar(15).amount, five.times(3).amount)
    def test_equality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        # триангуляция, создаем дополнительный пример для обобщения
        self.assertFalse(Dollar(5).equals(Dollar(6)))



if __name__ == "__main__":
    unittest.main()