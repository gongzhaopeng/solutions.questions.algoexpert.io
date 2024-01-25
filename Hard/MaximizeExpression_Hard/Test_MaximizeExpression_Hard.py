# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_MaximizeExpression_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [3, 6, 1, -3, 2, 7]
        expected = 4
        actual = program.maximizeExpression(input)
        self.assertEqual(actual, expected)
