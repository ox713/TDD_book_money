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
        self.assertEqual(Dollar(10).famount(), five.times(2).famount())
        product = five.times(3)
        self.assertEqual(Dollar(15).famount(), five.times(3).famount())
    def test_equality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        # триангуляция, создаем дополнительный пример для обобщения
        self.assertFalse(Dollar(5).equals(Dollar(6)))

    def test_mul_franc(self):
        five = Franc(5)
        self.assertEqual(Franc(10).famount(), five.times(2).famount())
        self.assertEqual(Franc(15).famount(), five.times(3).famount())




if __name__ == "__main__":
    unittest.main()