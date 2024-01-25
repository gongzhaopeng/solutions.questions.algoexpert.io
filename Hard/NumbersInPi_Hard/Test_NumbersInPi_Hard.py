# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_NumbersInPi_Hard as program
import unittest

PI = "3141592653589793238462643383279"


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        numbers = [
            "314159265358979323846",
            "26433",
            "8",
            "3279",
            "314159265",
            "35897932384626433832",
            "79",
        ]
        self.assertEqual(program.numbersInPi(PI, numbers), 2)
