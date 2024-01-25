# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_NextGreaterElement_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 5, -3, -4, 6, 7, 2]
        expected = [5, 6, 6, 6, 7, -1, 5]
        actual = program.nextGreaterElement(input)
        self.assertEqual(actual, expected)
