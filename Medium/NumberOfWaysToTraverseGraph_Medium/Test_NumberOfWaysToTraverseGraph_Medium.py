# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionIII_NumberOfWaysToTraverseGraph_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        width = 4
        height = 3
        expected = 10
        actual = program.numberOfWaysToTraverseGraph(width, height)
        self.assertEqual(actual, expected)
