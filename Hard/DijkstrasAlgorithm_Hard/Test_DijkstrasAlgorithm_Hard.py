# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_DijkstrasAlgorithm_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        start = 0
        edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
        expected = [0, 7, 13, 27, 10, -1]
        actual = program.dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        start = 7
        edges = [
            [
                [1, 1],
                [3, 1]
            ],
            [
                [2, 1]
            ],
            [
                [6, 1]
            ],
            [
                [1, 3],
                [2, 4],
                [4, 2],
                [5, 3],
                [6, 5]
            ],
            [
                [5, 1]
            ],
            [
                [4, 1]
            ],
            [
                [5, 2]
            ],
            [
                [0, 7]
            ]
        ]
        expected = [7, 8, 9, 8, 10, 11, 10, 0]
        actual = program.dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)
