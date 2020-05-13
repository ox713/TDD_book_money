import unittest
import os
import sys
# sys.path.append(os.getcwd())
from TDD import *

class TestTdd(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(Dollar(10)._amount, Dollar(5).times(2)._amount)
        self.assertEqual(Dollar(15)._amount, Dollar(5).times(3)._amount)

    def test_mul_Fr(self):
        self.assertEqual(Franc(10)._amount, Franc(5).times(2)._amount)
        self.assertEqual(Franc(15)._amount, Franc(5).times(3)._amount)

    def test_all_equality(self):
        self.assertTrue(Dollar(10).equals(Dollar(10)))
        self.assertFalse(Dollar(10).equals(Dollar(5)))
        self.assertTrue(Franc(10).equals(Franc(10)))
        self.assertFalse(Franc(10).equals(Franc(5)))
        # сранвиваем доллары и франки
        self.assertFalse(Dollar(10).equals(Franc(10)))



if __name__ == "__main__":
    unittest.main()