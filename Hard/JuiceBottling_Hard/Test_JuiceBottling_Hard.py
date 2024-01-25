# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_JuiceBottling_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [0, 2, 5, 6]
        expected = [1, 2]
        actual = program.juiceBottling(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [0, 2, 3, 4]
        expected = [1, 1, 1]
        actual = program.juiceBottling(input)
        self.assertEqual(actual, expected)
