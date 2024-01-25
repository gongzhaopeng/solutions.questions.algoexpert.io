# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_CommonCharacters_Easy as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["abc", "bcd", "cbad"]
        expected = ["b", "c"]
        actual = program.commonCharacters(input)
        actual.sort()
        self.assertEqual(actual, expected)
