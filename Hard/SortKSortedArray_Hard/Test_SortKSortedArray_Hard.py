# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_SortKSortedArray_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [3, 2, 1, 5, 4, 7, 6, 5]
        k = 3
        expected = [1, 2, 3, 4, 5, 5, 6, 7]
        actual = program.sortKSortedArray(input, k)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [-1, -5]
        k = 1
        expected = [-5, -1]
        actual = program.sortKSortedArray(input, k)
        self.assertEqual(actual, expected)
