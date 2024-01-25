# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_AmbiguousMeasurements_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        cups = [[200, 210], [450, 465], [800, 850]]
        low = 2100
        high = 2300
        expected = True
        actual = program.ambiguousMeasurements(cups, low, high)
        self.assertEqual(actual, expected)
