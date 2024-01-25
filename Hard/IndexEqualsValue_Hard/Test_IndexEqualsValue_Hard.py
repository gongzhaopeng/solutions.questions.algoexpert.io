# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_IndexEqualsValue_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-5, -3, 0, 3, 4, 5, 9]
        expected = 3
        actual = program.indexEqualsValue(array)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        array = []
        expected = -1
        actual = program.indexEqualsValue(array)
        self.assertEqual(actual, expected)
