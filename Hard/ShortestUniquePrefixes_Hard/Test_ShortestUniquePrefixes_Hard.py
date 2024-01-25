# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_ShortestUniquePrefixes_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        strings = ["algoexpert", "algorithm", "frontendexpert", "mlexpert"]
        expected = ["algoe", "algor", "f", "m"]
        actual = program.shortestUniquePrefixes(strings)
        self.assertEqual(actual, expected)
