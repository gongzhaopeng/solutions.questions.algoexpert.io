# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_WaterArea_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]), 48)

    def test_case_2(self):
        self.assertEqual(program.waterArea([]), 0)

    def test_case_3(self):
        self.assertEqual(program.waterArea([0, 1, 0, 1, 0, 2, 0, 3]), 4)
