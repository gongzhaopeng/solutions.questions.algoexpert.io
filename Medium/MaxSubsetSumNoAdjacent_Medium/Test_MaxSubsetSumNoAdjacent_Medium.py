# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_MaxSubsetSumNoAdjacent_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)
