# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_MinimumPassesOfMatrix_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1],
        ]
        expected = 3
        actual = program.minimumPassesOfMatrix(input)
        self.assertEqual(actual, expected)
