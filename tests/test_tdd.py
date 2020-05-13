import unittest
import os
import sys
# sys.path.append(os.getcwd())
from TDD import *

class TestTdd(unittest.TestCase):
    def test_mul(self):

        Money(10).dollar()
        self.assertEqual(Money(10).dollar()._amount, Money(5).times(2)._amount)
        self.assertEqual(Money(15).dollar()._amount, Money(5).times(3)._amount)
        self.assertEqual(Money(10).franc()._amount, Money(5).times(2)._amount)
        self.assertEqual(Money(15).franc()._amount, Money(5).times(3)._amount)

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

    def test_currency(self):
        self.assertEqual("USD", Dollar(1, "USD").dollar().currency())
        self.assertEqual("CHF", Dollar(1, "CHF").dollar().currency())





if __name__ == "__main__":
    unittest.main()