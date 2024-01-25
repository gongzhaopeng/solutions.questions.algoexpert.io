# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_BlackjackProbability_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        target = 21
        startingHand = 15
        expected = 0.45
        actual = program.blackjackProbability(target, startingHand)
        self.assertEqual(actual, expected)
