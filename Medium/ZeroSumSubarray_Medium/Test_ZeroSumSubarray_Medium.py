# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_ZeroSumSubarray_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [4, 2, -1, -1, 3]
        expected = True
        actual = program.zeroSumSubarray(input)
        self.assertEqual(actual, expected)
