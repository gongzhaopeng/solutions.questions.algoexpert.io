# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_MaximumSumSubmatrix_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[5, 3, -1, 5], [-7, 3, 7, 4], [12, 8, 0, 0], [1, -8, -8, 2]]
        size = 2
        expected = 18
        actual = program.maximumSumSubmatrix(matrix, size)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        matrix = [
            [3, -4, 6, -5, 1],
            [1, -2, 8, -4, -2],
            [3, -8, 9, 3, 1],
            [-7, 3, 4, 2, 7],
            [-3, 7, -5, 7, -6]
        ]
        size = 3
        expected = 28
        actual = program.maximumSumSubmatrix(matrix, size)
        self.assertEqual(actual, expected)
