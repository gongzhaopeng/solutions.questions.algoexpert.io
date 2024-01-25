# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_KruskalsAlgorithm_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[[1, 1]], [[0, 1]]]
        expected = [[[1, 1]], [[0, 1]]]
        actual = program.kruskalsAlgorithm(input)
        self.assertEqual(actual, expected)
