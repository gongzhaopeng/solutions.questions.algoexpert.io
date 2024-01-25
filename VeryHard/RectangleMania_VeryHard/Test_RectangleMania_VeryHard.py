# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_RectangleMania_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
        self.assertEqual(program.rectangleMania(coords), 6)

    def test_case_2(self):
        coords = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0],
            [2, 1],
            [2, 0],
            [3, 1],
            [3, 0],
            [1, 3],
            [3, 3],
            [0, -4],
            [3, -4]
        ]
        self.assertEqual(program.rectangleMania(coords), 10)
