# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_SquareOfZeros_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 1],
        ]
        self.assertEqual(program.squareOfZeroes(matrix), True)

    def test_case_2(self):
        matrix = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        self.assertEqual(program.squareOfZeroes(matrix), False)
