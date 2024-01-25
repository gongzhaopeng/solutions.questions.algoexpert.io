# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_CountInversions_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 3, 3, 1, 9, 5, 6]
        expected = 5
        actual = program.countInversions(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = []
        expected = 0
        actual = program.countInversions(input)
        self.assertEqual(actual, expected)
