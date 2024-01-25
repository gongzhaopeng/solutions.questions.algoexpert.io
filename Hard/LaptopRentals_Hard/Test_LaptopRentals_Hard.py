# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_LaptopRentals_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]
        expected = 3
        actual = program.laptopRentals(input)
        self.assertEqual(actual, expected)
