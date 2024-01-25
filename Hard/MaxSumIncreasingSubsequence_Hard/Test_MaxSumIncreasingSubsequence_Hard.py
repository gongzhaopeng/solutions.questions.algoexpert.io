# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_MaxSumIncreasingSubsequence_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            program.maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]),
            [110, [10, 20, 30, 50]],
        )
