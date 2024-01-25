# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_TwoEdgeConnectedGraph_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 2, 5], [0, 2], [0, 1, 3], [2, 4, 5], [3, 5], [0, 3, 4]]
        expected = True
        actual = program.twoEdgeConnectedGraph(input)
        self.assertEqual(actual, expected)
