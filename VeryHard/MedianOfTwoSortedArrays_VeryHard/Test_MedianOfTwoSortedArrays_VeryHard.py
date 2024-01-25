# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_MedianOfTwoSortedArrays_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrayOne = [1, 3, 4, 5]
        arrayTwo = [2, 3, 6, 7]
        expected = 3.5
        actual = program.medianOfTwoSortedArrays(arrayOne, arrayTwo)
        self.assertEqual(actual, expected)
