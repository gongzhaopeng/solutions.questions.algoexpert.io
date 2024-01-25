# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_MinNumberOfJumps_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)
