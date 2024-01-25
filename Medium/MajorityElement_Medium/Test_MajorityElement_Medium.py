# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_MajorityElement_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 2, 2, 1, 2]
        expected = 2
        actual = program.majorityElement(input)
        self.assertEqual(actual, expected)
