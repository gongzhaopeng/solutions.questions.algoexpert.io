# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionIII_OptimalAssemblyLine_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stepDurations = [15, 15, 30, 30, 45]
        numStations = 3
        expected = 60
        actual = program.optimalAssemblyLine(stepDurations, numStations)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        stepDurations = [6, 8, 4, 2, 10]
        numStations = 3
        expected = 12
        actual = program.optimalAssemblyLine(stepDurations, numStations)
        self.assertEqual(actual, expected)
