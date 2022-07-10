# Name: Xiao Yu Chen
# Course: CS362 Summer 2022
# Date: 7/8/2022

from contrived_func import contrived_func
import unittest


class ContrivedFuncCoverageTests(unittest.TestCase):
    def test_c1(self):
        val = 125
        self.assertTrue(contrived_func(val))

    def test_c2(self):
        val = 6
        self.assertFalse(contrived_func(val))

    def test_c3(self):
        val = 5
        self.assertTrue(contrived_func(val))

    def test_c4(self):
        val = 59
        self.assertFalse(contrived_func(val))

    def test_c5(self):
        val = 99
        self.assertFalse(contrived_func(val))

    def test_c6(self):
        val = 250
        self.assertTrue(contrived_func(val))

    def test_c7(self):
        val = 76
        self.assertFalse(contrived_func(val))


if __name__ == "__main__":
    unittest.main()
