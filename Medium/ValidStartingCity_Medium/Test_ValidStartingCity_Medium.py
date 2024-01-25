# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_ValidStartingCity_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        distances = [5, 25, 15, 10, 15]
        fuel = [1, 2, 1, 0, 3]
        mpg = 10
        expected = 4
        actual = program.validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)
