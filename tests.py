# Name: Xiao Yu Chen
# Course: CS362 Summer 2022
# Date: 7/8/2022

from contrived_func import contrived_func
import unittest


class ContrivedFuncCoverageTests(unittest.TestCase):
    # Tests True for (100, 150)
    def test_1(self):
        val = 125
        self.assertTrue(contrived_func(val))

    # Tests True for val == 6
    def test_2(self):
        val = 6
        self.assertFalse(contrived_func(val))

    # Tests False for val == 6
    def test_3(self):
        val = 5
        self.assertTrue(contrived_func(val))

    # Tests True for first inequality and False for the second
    def test_4(self):
        val = 59
        self.assertFalse(contrived_func(val))

    # Tests False for the modulus
    def test_5(self):
        val = 99
        self.assertFalse(contrived_func(val))

    # Tests True for the modulus
    def test_6(self):
        val = 250
        self.assertTrue(contrived_func(val))

    # Tests False for the first 'or' inequality
    def test_7(self):
        val = 75
        self.assertTrue(contrived_func(val))


if __name__ == "__main__":
    unittest.main()
