# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_KnapsackProblem_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            program.knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]]
        )

    def test_case_2(self):
        capacity = 200
        items = [
            [465, 100],
            [400, 85],
            [255, 55],
            [350, 45],
            [650, 130],
            [1000, 190],
            [455, 100],
            [100, 25],
            [1200, 190],
            [320, 65],
            [750, 100],
            [50, 45],
            [550, 65],
            [100, 50],
            [600, 70],
            [240, 40]
        ]
        self.assertEqual(
            program.knapsackProblem(items, capacity), [1500, [3, 12, 14]]
        )
