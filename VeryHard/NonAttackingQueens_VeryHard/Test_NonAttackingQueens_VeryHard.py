# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_NonAttackingQueens_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = 4
        expected = 2
        actual = program.nonAttackingQueens(input)
        self.assertEqual(actual, expected)
