# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_A_Star_Algorithm_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        startRow = 0
        startCol = 1
        endRow = 4
        endCol = 3
        graph = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0],
        ]
        expected = [[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]
        actual = program.aStarAlgorithm(startRow, startCol, endRow, endCol, graph)
        self.assertEqual(actual, expected)
