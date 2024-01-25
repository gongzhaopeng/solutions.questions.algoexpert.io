# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionIII_DetectArbitrage_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1.0, 0.8631, 0.5903], [1.1586, 1.0, 0.6849], [1.6939, 1.46, 1.0]]
        expected = True
        actual = program.detectArbitrage(input)
        self.assertEqual(actual, expected)
