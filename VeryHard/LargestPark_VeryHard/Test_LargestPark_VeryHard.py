# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_LargestPark_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        land = [
            [False, True, True, True, False],
            [False, False, False, True, False],
            [False, False, False, False, False],
            [False, True, True, True, True],
        ]
        expected = 6
        actual = program.largestPark(land)
        self.assertEqual(actual, expected)
