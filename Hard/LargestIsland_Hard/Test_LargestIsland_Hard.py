# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_LargestIsland_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[0, 1, 1], [0, 0, 1], [1, 1, 0]]
        expected = 5
        actual = program.largestIsland(input)
        self.assertEqual(actual, expected)
