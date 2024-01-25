# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_LongestCommonSubsequence_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = program.longestCommonSubsequence("ZXVVYZW", "XKYKZPW")
        self.assertEqual(output, ["X", "Y", "Z", "W"])
