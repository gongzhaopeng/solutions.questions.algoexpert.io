# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionIII_MissingNumbers_Easy as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [4, 5, 1, 3]
        expected = [2, 6]
        actual = program.missingNumbers(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [3]
        expected = [1, 2]
        actual = program.missingNumbers(input)
        self.assertEqual(actual, expected)
