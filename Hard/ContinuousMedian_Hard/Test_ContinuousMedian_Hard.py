# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_ContinuousMedian_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        handler = program.ContinuousMedianHandler()
        handler.insert(5)
        handler.insert(10)
        self.assertEqual(handler.getMedian(), 7.5)
        handler.insert(100)
        self.assertEqual(handler.getMedian(), 10)
