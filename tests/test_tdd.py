import unittest
import os
import sys
# sys.path.append(os.getcwd())
from TDD import *

class TestTdd(unittest.TestCase):
    def test_mul(self):

        self.assertEqual(Money(10, "USD")._amount, Money(5, "USD").times(2)._amount)
        self.assertEqual(Money(10, "USD")._amount, Money(5, "USD").times(2)._amount)
        self.assertEqual(Money(10, "CHF")._amount, Money(5, "CHF").times(2)._amount)
        self.assertEqual(Money(10, "CHF")._amount, Money(5, "CHF").times(2)._amount)


    def test_all_equality(self):
        self.assertTrue(Money(10, "USD").equals(Money(10, "USD")))
        self.assertFalse(Money(10, "USD").equals(Money(5, "USD")))
        self.assertTrue(Money(10, "CHF").equals(Money(10, "CHF")))
        self.assertFalse(Money(10, "CHF").equals(Money(5, "CHF")))
        # сранвиваем доллары и франки
        self.assertFalse(Money(10, "USD").equals(Money(10, "CHF")))

    def test_currency(self):
        self.assertEqual("USD", Money(1, "USD").currency())
        self.assertEqual("CHF", Money(1, "CHF").currency())





if __name__ == "__main__":
    unittest.main()