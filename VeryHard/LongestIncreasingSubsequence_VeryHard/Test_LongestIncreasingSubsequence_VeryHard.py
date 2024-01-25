# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_LongestIncreasingSubsequence_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            program.longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]),
            [-24, 2, 3, 5, 6, 35],
        )

    def test_case_2(self):
        self.assertEqual(
            program.longestIncreasingSubsequence([-1, 2]),
            [-1, 2],
        )
