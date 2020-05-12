import unittest
import os
import sys
# sys.path.append(os.getcwd())
from TDD import *


class TestTdd(unittest.TestCase):
    def test_mul(self):
        # дублирование 5*2
        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)


if __name__ == "__main__":
    unittest.main()