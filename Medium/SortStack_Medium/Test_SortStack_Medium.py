# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_SortStack_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [-5, 2, -2, 4, 3, 1]
        expected = [-5, -2, 1, 2, 3, 4]
        actual = program.sortStack(input)
        self.assertEqual(actual, expected)
