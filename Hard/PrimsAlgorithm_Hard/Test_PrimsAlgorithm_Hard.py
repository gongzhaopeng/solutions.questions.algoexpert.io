# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_PrimsAlgorithm_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[[1, 1]], [[0, 1]]]
        expected = [[[1, 1]], [[0, 1]]]
        actual = program.primsAlgorithm(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [
            [
                [1, 3],
                [2, 5]
            ],
            [
                [0, 3],
                [2, 10],
                [3, 12]
            ],
            [
                [0, 5],
                [1, 10]
            ],
            [
                [1, 12]
            ]
        ]
        expected = [
            [
                [1, 3],
                [2, 5]
            ],
            [
                [0, 3],
                [3, 12]
            ],
            [
                [0, 5]
            ],
            [
                [1, 12]
            ]
        ]
        actual = program.primsAlgorithm(input)
        self.assertEqual(actual, expected)
