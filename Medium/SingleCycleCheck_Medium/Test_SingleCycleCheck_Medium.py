# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_SingleCycleCheck_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.hasSingleCycle([2, 3, 1, -4, -4, 2]), True)

    def test_case_2(self):
        self.assertEqual(program.hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 909, -26]), False)
