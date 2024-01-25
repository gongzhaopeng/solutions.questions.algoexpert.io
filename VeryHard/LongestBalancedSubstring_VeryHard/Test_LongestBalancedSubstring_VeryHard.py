# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionIII_LongestBalancedSubstring_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "(()))("
        expected = 4
        actual = program.longestBalancedSubstring(string)
        self.assertEqual(actual, expected)
