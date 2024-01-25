# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionIII_LongestPalindromicSubstring_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.longestPalindromicSubstring("abaxyzzyxf"), "xyzzyx")

    def test_case_2(self):
        self.assertEqual(program.longestPalindromicSubstring("z234a5abbba54a32z"), "5abbba5")

    def test_case_3(self):
        self.assertEqual(program.longestPalindromicSubstring("a"), "a")
